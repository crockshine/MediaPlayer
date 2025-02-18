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
            def find_size(size_bytes):
                res = 0
                for b in size_bytes:
                    res = res << 7 | (b & 0x7F) # маска 01111111
                return res

            f.seek(0, 0)
            tag_head_bytes = f.read(10)
            version_byte = tag_head_bytes[3]
            flag_byte = tag_head_bytes[5]
            flags = {
                "Unsync": flag_byte & 0b10000000 != 0,
                "Extended header":flag_byte  & 0b01000000 != 0,
                "Experimental tag": flag_byte & 0b00100000 != 0,
                # флаг present footer можно проигнорировать
            }
            frame_size = find_size(tag_head_bytes[6:10])
            frames = None

            if flags["Extended header"]:
                f.seek(10)
                extended_bytes = f.read(4)

                if version_byte == 3:
                    extended_size = int.from_bytes(extended_bytes, 'big')
                    f.seek(10+extended_size)
                    frames = f.read(frame_size - extended_size)
                elif version_byte == 4:
                    res_in_bytes = 0
                    for byte in extended_bytes:
                        res_in_bytes = res_in_bytes << 7 | (byte & 0x7F)
                    extended_size = res_in_bytes
                    f.seek(10 + extended_size)
                    frames = f.read(frame_size - extended_size)
                    # вопрос - правильно ли тут?

            if flags["Unsync"]:
                new_data = bytearray()
                i = 0
                while i < len(frames) - 1:
                    if not (frames[i] == 0x00 and frames[i + 1] == 0xFF):
                        new_data.append(frames[i])
                    i += 1
                new_data.append(frames[-1])  # Добавляем последний байт
                frames = new_data



            print('version - ',version_byte, 'flag - ', flag_byte,'size', frame_size, 'FRAMES - ', frames)

        else:
            file_name = os.path.basename(fp)
            return {"title": file_name.split('.')[0], "author": 'Автор не указан'}

