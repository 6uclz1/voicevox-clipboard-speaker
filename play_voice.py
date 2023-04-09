import wave
import pyaudio

"""
作成した音声ファイルを再生する
"""
def play_voice(file_parh):
    with wave.open(file_parh, 'rb') as wf:
        # PyAudioのストリームを開く
        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(2),
            channels=1,
            rate=24000,
            output=True
        )

        # 音声をストリームに書き込んで再生する
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # ストリームを閉じる
        stream.stop_stream()
        stream.close()
        p.terminate()