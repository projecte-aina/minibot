# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stt_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11stt_service.proto\x12\x0bvosk.stt.v1\x1a\x1egoogle/protobuf/duration.proto\"}\n\x1bStreamingRecognitionRequest\x12\x30\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x1e.vosk.stt.v1.RecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"r\n\x1cStreamingRecognitionResponse\x12\x33\n\x06\x63hunks\x18\x01 \x03(\x0b\x32#.vosk.stt.v1.SpeechRecognitionChunkJ\x04\x08\x02\x10\x03R\x17\x65nd_of_single_utterance\"H\n\x11RecognitionConfig\x12\x33\n\rspecification\x18\x01 \x01(\x0b\x32\x1c.vosk.stt.v1.RecognitionSpec\"\xf7\x02\n\x0fRecognitionSpec\x12\x42\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32*.vosk.stt.v1.RecognitionSpec.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x03\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x18\n\x10profanity_filter\x18\x04 \x01(\x08\x12\r\n\x05model\x18\x05 \x01(\t\x12\x17\n\x0fpartial_results\x18\x07 \x01(\x08\x12\x18\n\x10single_utterance\x18\x08 \x01(\x08\x12\x13\n\x0braw_results\x18\n \x01(\x08\x12\x18\n\x10max_alternatives\x18\x0b \x01(\x05\x12 \n\x18\x65nable_word_time_offsets\x18\x0c \x01(\x08\"A\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x10\n\x0cLINEAR16_PCM\x10\x01\"\x82\x01\n\x16SpeechRecognitionChunk\x12?\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32).vosk.stt.v1.SpeechRecognitionAlternative\x12\r\n\x05\x66inal\x18\x02 \x01(\x08\x12\x18\n\x10\x65nd_of_utterance\x18\x03 \x01(\x08\"f\n\x1cSpeechRecognitionAlternative\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12$\n\x05words\x18\x03 \x03(\x0b\x32\x15.vosk.stt.v1.WordInfo\"\x88\x01\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x32}\n\nSttService\x12o\n\x12StreamingRecognize\x12(.vosk.stt.v1.StreamingRecognitionRequest\x1a).vosk.stt.v1.StreamingRecognitionResponse\"\x00(\x01\x30\x01\x62\x06proto3')



_STREAMINGRECOGNITIONREQUEST = DESCRIPTOR.message_types_by_name['StreamingRecognitionRequest']
_STREAMINGRECOGNITIONRESPONSE = DESCRIPTOR.message_types_by_name['StreamingRecognitionResponse']
_RECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['RecognitionConfig']
_RECOGNITIONSPEC = DESCRIPTOR.message_types_by_name['RecognitionSpec']
_SPEECHRECOGNITIONCHUNK = DESCRIPTOR.message_types_by_name['SpeechRecognitionChunk']
_SPEECHRECOGNITIONALTERNATIVE = DESCRIPTOR.message_types_by_name['SpeechRecognitionAlternative']
_WORDINFO = DESCRIPTOR.message_types_by_name['WordInfo']
_RECOGNITIONSPEC_AUDIOENCODING = _RECOGNITIONSPEC.enum_types_by_name['AudioEncoding']
StreamingRecognitionRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONREQUEST,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.StreamingRecognitionRequest)
  })
_sym_db.RegisterMessage(StreamingRecognitionRequest)

StreamingRecognitionResponse = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESPONSE,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.StreamingRecognitionResponse)
  })
_sym_db.RegisterMessage(StreamingRecognitionResponse)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONCONFIG,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.RecognitionConfig)
  })
_sym_db.RegisterMessage(RecognitionConfig)

RecognitionSpec = _reflection.GeneratedProtocolMessageType('RecognitionSpec', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONSPEC,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.RecognitionSpec)
  })
_sym_db.RegisterMessage(RecognitionSpec)

SpeechRecognitionChunk = _reflection.GeneratedProtocolMessageType('SpeechRecognitionChunk', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONCHUNK,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.SpeechRecognitionChunk)
  })
_sym_db.RegisterMessage(SpeechRecognitionChunk)

SpeechRecognitionAlternative = _reflection.GeneratedProtocolMessageType('SpeechRecognitionAlternative', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONALTERNATIVE,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.SpeechRecognitionAlternative)
  })
_sym_db.RegisterMessage(SpeechRecognitionAlternative)

WordInfo = _reflection.GeneratedProtocolMessageType('WordInfo', (_message.Message,), {
  'DESCRIPTOR' : _WORDINFO,
  '__module__' : 'stt_service_pb2'
  # @@protoc_insertion_point(class_scope:vosk.stt.v1.WordInfo)
  })
_sym_db.RegisterMessage(WordInfo)

_STTSERVICE = DESCRIPTOR.services_by_name['SttService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STREAMINGRECOGNITIONREQUEST._serialized_start=66
  _STREAMINGRECOGNITIONREQUEST._serialized_end=191
  _STREAMINGRECOGNITIONRESPONSE._serialized_start=193
  _STREAMINGRECOGNITIONRESPONSE._serialized_end=307
  _RECOGNITIONCONFIG._serialized_start=309
  _RECOGNITIONCONFIG._serialized_end=381
  _RECOGNITIONSPEC._serialized_start=384
  _RECOGNITIONSPEC._serialized_end=759
  _RECOGNITIONSPEC_AUDIOENCODING._serialized_start=694
  _RECOGNITIONSPEC_AUDIOENCODING._serialized_end=759
  _SPEECHRECOGNITIONCHUNK._serialized_start=762
  _SPEECHRECOGNITIONCHUNK._serialized_end=892
  _SPEECHRECOGNITIONALTERNATIVE._serialized_start=894
  _SPEECHRECOGNITIONALTERNATIVE._serialized_end=996
  _WORDINFO._serialized_start=999
  _WORDINFO._serialized_end=1135
  _STTSERVICE._serialized_start=1137
  _STTSERVICE._serialized_end=1262
# @@protoc_insertion_point(module_scope)
