# pip
import pyperclip
from ulid import ULID

# local module
from synthesis import synthesis
from play_voice import play_voice
from split_text import split_text

def main():
    last_content = pyperclip.paste()
    while True:
        current_content = pyperclip.paste()
        if current_content != last_content:
            last_content = current_content
            for t in split_text(current_content):
                ulid = ULID()
                synthesis(t, f"./voice/audio_{str(ulid)}.wav")
                play_voice(f"./voice/audio_{str(ulid)}.wav")

if __name__ == '__main__':
    main()
