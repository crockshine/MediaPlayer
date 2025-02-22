from utils.mp3 import is_id3v1
from utils.mp3 import is_id3v2
import os
import io  # Для работы с байтовыми данными как с файлом


def read_mp3(fp):
    # Пример тестовых байтов (ID3v2.2 без флагов)
    test_bytes =  b"ID3" + b"\x04\x00" + b"\x40" + b"\x00\x00\x00\x0F" +b"TIT2" + b"\x00\x00\x00\x05" + b"\x00\x00" + b"Title" +b"FOOTER1234"
    with io.BytesIO(test_bytes) as f:
        print(f.getvalue())

        if is_id3v1(f):  # первая версия тега
            f.seek(-128, 2)
            tag_data = f.read(128)

            title = tag_data[3:33].decode("latin-1").strip("\x00")
            artist = tag_data[33:63].decode("latin-1").strip("\x00")

            return {"title": title, "author": artist}
        elif is_id3v2(f):
            def find_size(size_bytes):
                res = 0
                for b in size_bytes:
                    res = res << 7 | (b & 0x7F)  # маска 01111111
                return res

            def is_frame_id(data):
                res = False
                for byte in data:
                    if 65 <= byte <= 90 or 48 <= byte <= 57:
                        return True
                    else:
                        res = False
                return res

            f.seek(0, 0)

            tag_head_bytes = f.read(10)
            version_byte = tag_head_bytes[3]
            flag_byte = tag_head_bytes[5]
            flags = {
                "Unsync": bool(flag_byte & 0b10000000 != 0),
                "Extended header": bool(False)
                # расширеный заголвоок далее определяется по 4 байтам после основного заголовка
            }
            frame_size = find_size(tag_head_bytes[6:10])
            print(frame_size)
            print('flags ', flags)
            frames = None

            # проверка на расширеный заголовок. 3 версия - bigint, 4 - syncsafe
            f.seek(10)
            extended_bytes = f.read(4)
            print(extended_bytes)
            if not is_frame_id(extended_bytes):
                flags["Extended header"] = True

                if version_byte == 3:
                    extended_size = int.from_bytes(extended_bytes, 'big')
                    f.seek(10 + 4 + extended_size)
                    frames = f.read(frame_size - extended_size)
                    print('extended_size v3', extended_size)
                if version_byte == 4:
                    extended_size = find_size(extended_bytes)
                    f.seek(10 + 4 + extended_size)
                    frames = f.read(frame_size - extended_size)
                    print('extended_size v4', extended_size)
            else:
                f.seek(10)
                frames = f.read(frame_size)

            if flags["Unsync"]:
                print('АНСИХ')
                new_data = bytearray()
                i = 0
                while i < len(frames) - 1:
                    if not (frames[i] == 0x00 and frames[i + 1] == 0xFF):
                        new_data.append(frames[i])
                    i += 1
                new_data.append(frames[-1])  # Добавляем последний байт
                frames = bytes(new_data)
            else:
                if not flags["Extended header"]:
                    f.seek(10)
                    frames = f.read(frame_size)

            print(frames)

        else:
            file_name = os.path.basename(fp)
            return {"title": file_name.split('.')[0], "author": 'Автор не указан'}

read_mp3('')