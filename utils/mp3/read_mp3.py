import io
import os
import zlib

from utils.mp3 import (
    is_id3v1,
    is_id3v2,
    get_frames_from_id3v2,
    parse_frames_v1_2,
    parse_frames_v4,
    parse_frames_v3
)


def read_mp3(fp):
    # with (open(fp, "rb") as f):
    # #### находим дефолтное название, если название не будет найдено
    # file_name = os.path.basename(fp)
    #
    # def get_substring_before_last_dot(s):
    #     last_dot_index = s.rfind('.') #макс вхождение
    #     if last_dot_index != -1:
    #         return s[:last_dot_index]
    #     return s
    #
    # default_title = get_substring_before_last_dot(file_name)
    # ################################################################
    default_title = 'asdasdsa'
    fake_mp3_data = (
        b"ID3"
        b"\x04\x00"
        b"\x80"         # Флаг Unsynchronisation (глобальный)
        b"\x00\x00\x00\x0F" # Размер тега (синхронизированный)
        b"TIT2"
        b"\x00\x00\x00\x0A" # Размер данных (10 байт)
        b"\x00\x08"         # Флаги: Unsynchronisation (локальный)
        b"\x03"             # Кодировка UTF-8
        b"Test\xFF\x00Title" # Данные с лишним 0x00
    )

    f = io.BytesIO(fake_mp3_data)
    if is_id3v2(f):

        [frames, version] = get_frames_from_id3v2(f)
        print(frames)

        if version == 1 or version == 2:
            [title, author] = parse_frames_v1_2(frames)
            return {"title": title if title is not None else default_title,
                    "author": author if author is not None else 'Автор не найден'}
        elif version == 3:
            [title, author] = parse_frames_v3(frames)
            return {"title": title if title is not None else default_title,
                    "author": author if author is not None else 'Автор не найден'}
        elif version == 4:
            [title, author] = parse_frames_v4(frames)
            return {"title": title if title is not None else 'Без названия',
                    "author": author if author is not None else 'Автор не найден'}

    elif is_id3v1(f):  # первая версия тега
        print('idv1')
        f.seek(-128, 2)
        tag_data = f.read(128)

        print(tag_data[3:33], 'тег дата')
        title = tag_data[3:33].decode("latin-1").strip("\x00")
        artist = tag_data[33:63].decode("latin-1").strip("\x00")

        return {"title": title if len(title) > 0 else default_title,
                "author": artist if len(artist) > 0 else "Автор не найден"}
    else:
        return {"title": default_title, "author": 'Автор не найден'}


print(read_mp3(''))
