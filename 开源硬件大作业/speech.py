from aip import AipSpeech
import os
import pyaudio
import wave

# 录音
def record_sound():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8000
    RECORD_SECONDS = 3 # 设置录制秒数
    WAVE_OUTPUT_FILENAME = "audio.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    stream.start_stream()
    print("* 开始录音......")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# 语音识别
def recogize_speech():
    APP_ID = '33390815'
    API_KEY = "QnStCAuuFWxQxGqaqNs8yXZX"
    SECRET_KEY = "ncAslLWdpqVtq0T40l8dfOriFGG8p61T" 

    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

    with open('audio.wav', 'rb') as fp:
            wave=fp.read()

    print("* 正在识别......",len(wave))
    result = client.asr(wave, 'wav', 16000, {'dev_pid':1537})
    # print(result)
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        raise RecognizeError("Please check your network connection or record devices")

# 设置在识别命令出错时的报错
class RecognizeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
