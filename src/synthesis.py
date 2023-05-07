import requests
import json

# Voicevoxで音声ファイルを作成する
def synthesis(text, filename, speaker=14):
    print(text)
    
    # 音声合成用のクエリを作成する
    audio_query_response = requests.post(
        "http://127.0.0.1:50021/audio_query",
        params={"text": 'えっと、' + text, "speaker": speaker}
    )

    # 音声合成する
    synth_payload_response = requests.post(
        "http://127.0.0.1:50021/synthesis",
        params={"speaker": speaker},
        data=json.dumps(audio_query_response.json())
    )
    # 音声データを作成する
    with open(filename, "wb") as fp:
        fp.write(synth_payload_response.content)