from utils.mp3 import is_id3v1
from utils.mp3 import is_id3v2
import os

def read_mp3(fp):
    with open(fp, "rb") as f:
        if is_id3v1(f):
            f.seek(-128, 2)
        elif is_id3v2(f):
            f.seek(128, 0)
        else:
            file_name = os.path.basename(fp)
            return {"title": file_name.split('.')[0], "author": 'Автор не указан'}

        tag_data = f.read(128)
        print(tag_data)

    title = tag_data[3:33].decode("latin-1").strip("\x00")
    artist = tag_data[33:63].decode("latin-1").strip("\x00")

    if title == '': title = 'Название не указано'
    if artist == '': artist = 'Автор не указан'

    return {"title": title, "author": artist}