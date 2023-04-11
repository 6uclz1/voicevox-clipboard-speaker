"""
文字列を分割する
"""
def split_text(text):
    # 改行で区切る、空文字は除去する
    texts = text.splitlines()
    texts = filter(lambda a: a != '', texts)
    return texts