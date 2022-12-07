import os
import wave
import grpc

#from utils import GracefulKiller
from service.proto.stt.stt_service_pb2 import RecognitionSpec, RecognitionConfig, StreamingRecognitionRequest
from service.proto.stt.stt_service_pb2_grpc import SttServiceStub

#killer = GracefulKiller()

vosk_server_host = os.getenv('VOSK_SERVER_HOST', '127.0.0.1')
vosk_server_port = os.getenv('VOSK_SERVER_PORT', 5001)
channel = grpc.insecure_channel(f"{vosk_server_host}:{vosk_server_port}")

def gen(audio_file_name):
    specification = RecognitionSpec(
        partial_results=False,
        audio_encoding='LINEAR16_PCM',
        sample_rate_hertz=16000,
        enable_word_time_offsets=True,
        max_alternatives=1,
    )
    streaming_config = RecognitionConfig(specification=specification)

    yield StreamingRecognitionRequest(config=streaming_config)

    wf = wave.open(audio_file_name, "rb")
    frames_to_read = wf.getframerate() * 0.2
    while True:
        data = wf.readframes(int(frames_to_read))
        if len(data) == 0:
            break
        yield StreamingRecognitionRequest(audio_content=data)
    wf.close()


def transcribe(audio_file_name):
    stub = SttServiceStub(channel)
    it = stub.StreamingRecognize(gen(audio_file_name))

    try:
        for r in it:
            try:
                if (len(r.chunks) > 0):
                    text = r.chunks[0].alternatives[0].text
                    start = r.chunks[0].alternatives[0].words[0].start_time.seconds + r.chunks[0].alternatives[0].words[0].start_time.nanos/1000000000
                    end = r.chunks[0].alternatives[0].words[-1].end_time.seconds + r.chunks[0].alternatives[0].words[-1].end_time.nanos/1000000000
                    yield (text, start, end)
            except LookupError:
                pass
    except grpc._channel._Rendezvous as err:
        print('Error code %s, message: %s' % (err._state.code, err._state.details))
