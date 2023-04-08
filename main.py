import requests
import json
import pyperclip
import wave
import pyaudio

last_content = pyperclip.paste()

# Voicevoxで音声ファイルを作成する
def synthesis(text, filename, speaker=14):
    # 音声合成用のクエリを作成する
    audio_query_response = requests.post(
        "http://localhost:50021/audio_query",
        params={"text": 'えっと、' + text, "speaker": speaker}
    )

    # 音声合成する
    synth_payload_response = requests.post(
        "http://localhost:50021/synthesis",
        params={"speaker": speaker},
        data=json.dumps(audio_query_response.json())
    )
    # 音声データを作成する
    with open(filename, "wb") as fp:
        fp.write(synth_payload_response.content)

# 作成した音声ファイルを再生する
def play(file_parh):
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

def text_to_speech(text):
    # 改行で一旦音声生成を区切る、空文字は除去する
    texts = text.splitlines()
    texts = filter(lambda a: a != '', texts)

    for i, t in enumerate(texts):
        print(t)
        synthesis(t, f"audio_{i}.wav")
        play(f"audio_{i}.wav")

while True:
    current_content = pyperclip.paste()
    if current_content != last_content:
        print('!')
        last_content = current_content
        text_to_speech(current_content)