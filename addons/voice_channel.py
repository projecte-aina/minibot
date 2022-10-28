import logging
import uuid
import base64
from typing import Any, Awaitable, Callable, Dict, Iterable, List, Optional, Text

from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import UserMessage, OutputChannel

from sanic import Blueprint, response
from sanic.request import Request
#from sanic.response import HTTPResponse
from socketio import AsyncServer

logger = logging.getLogger(__name__)

class SocketVoiceBlueprint(Blueprint):
    def __init__(self, sio: AsyncServer, socketio_path, *args, **kwargs):
        self.sio = sio
        self.socketio_path = socketio_path
        super(SocketBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options):
        self.sio.attach(app, self.socketio_path)
        super(SocketBlueprint, self).register(app, options)

class SocketIOVoiceOutput(OutputChannel):
    @classmethod
    def name(cls) -> Text:
        return "socketiovoice"

    def __init__(self, sio: AsyncServer, bot_message_evt: Text, tts_url: Text, tts_voice: Text) -> None:
        self.sio = sio
        self.bot_message_evt = bot_message_evt
        self.tts_url = tts_url
        self.tts_voice = tts_voice

    async def _send_audio_message(self, socket_id: Text, response: Any) -> None:
        """Sends a message to the recipient using the bot event."""

        if response.get("text"):
          q = {
            'text': response['text']
          }
          if self.tts_voice:
            q['speaker_id'] = self.tts_voice
            q['style_wav']= None

          audioEndpoint = f"{self.tts_url}/api/tts/?{urlencode(q)}"
          audio = urlopen(audioEndpoint).read()
          logger.debug(f"_send_message- Calling Speech Endpoint: {audioEndpoint}")

          audioBase64 = base64.b64encode(audio).decode('ascii')
          audioUri = "data:audio/wav;base64," + audioBase64
          response['link'] = audioUri

        await self.sio.emit(self.bot_message_evt, response, room=socket_id)

    async def send_text_message(
        self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        """Send a message through this channel."""

        for message_part in text.strip().split("\n\n"):
            await self._send_audio_message(recipient_id, {"text": message_part})

class SocketIOVoiceInput(InputChannel):
    """A socket.io input channel."""

    @classmethod
    def name(cls) -> Text:
        return "socketiovoice"

    @classmethod
    def from_credentials(cls, credentials: Optional[Dict[Text, Any]]) -> InputChannel:
        credentials = credentials or {}
        return cls(
            credentials.get("user_message_evt", "user_uttered"),
            credentials.get("bot_message_evt", "bot_uttered"),
            credentials.get("namespace"),
            credentials.get("session_persistence", False),
            credentials.get("socketio_path", "/socket.io"),
            credentials.get("tts_url"),
            credentials.get("tts_voice"),
        )

    def __init__(
        self,
        user_message_evt: Text = "user_uttered",
        bot_message_evt: Text = "bot_uttered",
        namespace: Optional[Text] = None,
        session_persistence: bool = False,
        socketio_path: Optional[Text] = "/socket.io",
        tts_url: Text = None,
        tts_voice: Optional[Text] = False,
    ):
        self.bot_message_evt = bot_message_evt
        self.session_persistence = session_persistence
        self.user_message_evt = user_message_evt
        self.namespace = namespace
        self.socketio_path = socketio_path
        self.tts_url = tts_url
        self.tts_voice = tts_voice
        self.sio = None

    '''
    def get_output_channel(self) -> Optional["OutputChannel"]:
        if self.sio is None:
            rasa.shared.utils.io.raise_warning(
                "SocketIO output channel cannot be recreated. "
                "This is expected behavior when using multiple Sanic "
                "workers or multiple Rasa Open Source instances. "
                "Please use a different channel for external events in these "
                "scenarios."
            )
            return
        return SocketIOVoiceOutput(self.sio, self.bot_message_evt, self.tts_url, self.tts_voice)
    '''

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[Any]]
    ) -> Blueprint:
        # Workaround so that socketio works with requests from other origins.
        # https://github.com/miguelgrinberg/python-socketio/issues/205#issuecomment-493769183
        sio = AsyncServer(async_mode="sanic", cors_allowed_origins=[])
        socketio_webhook = SocketVoiceBlueprint(
            sio, self.socketio_path, "socketio_webhook", __name__
        )

        # make sio object static to use in get_output_channel
        self.sio = sio

        @socketio_webhook.route("/", methods=["GET"])
        async def health(_: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @sio.on("connect", namespace=self.namespace)
        async def connect(sid: Text, _) -> None:
            logger.debug(f"User {sid} connected to socketIO endpoint.")

        @sio.on("disconnect", namespace=self.namespace)
        async def disconnect(sid: Text) -> None:
            logger.debug(f"User {sid} disconnected from socketIO endpoint.")

        @sio.on("session_request", namespace=self.namespace)
        async def session_request(sid: Text, data: Optional[Dict]):
            if data is None:
                data = {}
            if "session_id" not in data or data["session_id"] is None:
                data["session_id"] = uuid.uuid4().hex
            if self.session_persistence:
                sio.enter_room(sid, data["session_id"])
            await sio.emit("session_confirm", data["session_id"], room=sid)
            logger.debug(f"User {sid} connected to socketIO endpoint.")


    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[Any]]
    ) -> Blueprint:
        # Workaround so that socketio works with requests from other origins.
        # https://github.com/miguelgrinberg/python-socketio/issues/205#issuecomment-493769183
        sio = AsyncServer(async_mode="sanic", cors_allowed_origins=[])
        socketio_webhook = SocketVoiceBlueprint(
            sio, self.socketio_path, "socketio_webhook", __name__
        )

        # make sio object static to use in get_output_channel
        self.sio = sio

        @socketio_webhook.route("/", methods=['GET'])
        async def health(request):
            return response.json({"status": "ok"})

        @sio.on('connect', namespace=self.namespace)
        async def connect(sid, environ):
            logger.debug("User {} connected to socketIO endpoint.".format(sid))
            print('Connected!')

        @sio.on('disconnect', namespace=self.namespace)
        async def disconnect(sid):
            logger.debug("User {} disconnected from socketIO endpoint."
                         "".format(sid))

        @sio.on('session_request', namespace=self.namespace)
        async def session_request(sid, data):
            print('This is sessioin request')

            if data is None:
                data = {}
            if 'session_id' not in data or data['session_id'] is None:
                data['session_id'] = uuid.uuid4().hex
            await sio.emit("session_confirm", data['session_id'], room=sid)
            logger.debug("User {} connected to socketIO endpoint."
                         "".format(sid))

        @sio.on('user_uttered', namespace=self.namespace)
        async def handle_message(sid, data):

            output_channel = SocketIOOutput(sio, sid, self.bot_message_evt, data['message'])
            if data['message'] == "/get_started":
                message = data['message']
            else:
                ##receive audio
                received_file = "output_{0}.wav".format(sid)
                logger.info(f"Audio file {received_file} received")

                urllib.request.urlretrieve(data['message'], received_file)
                path = os.path.dirname(__file__)
                if not os.path.isfile(path):
                    logger.info(f" file does not exist.")

                fs, audio = wav.read(received_file)
                #message = ds.stt(audio, fs)
                message = "Bon dia!"

                await sio.emit(self.user_message_evt, {"text":message}, room=sid)


            message_rasa = UserMessage(message, output_channel, sid,
                                  input_channel=self.name())
            await on_new_message(message_rasa)

        return socketio_webhook
