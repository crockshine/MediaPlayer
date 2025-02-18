from utils.mp3 import is_id3v1
from utils.mp3 import is_id3v2
import os

def read_mp3(fp):
    with open(fp, "rb") as f:
        if is_id3v1(f):
            f.seek(-128, 2)
            tag_data = f.read(128)

            title = tag_data[3:33].decode("latin-1").strip("\x00")
            artist = tag_data[33:63].decode("latin-1").strip("\x00")

            return {"title": title, "author": artist}
        elif is_id3v2(f):
            f.seek(0, 0)
            tag_head = f.read(10)
            print(tag_head)
            version = tag_head[3]
            flag = tag_head[5]

            def find_size(size_bytes):
                res = 0
                for byte in size_bytes:
                    res = res << 7 | (byte & 0x7F) #маска 01111111
                return res

            frame_size = find_size(tag_head[6:10+1])


            print('version - ',version, 'flag - ',flag,'size', frame_size)

        else:
            file_name = os.path.basename(fp)
            return {"title": file_name.split('.')[0], "author": 'Автор не указан'}

