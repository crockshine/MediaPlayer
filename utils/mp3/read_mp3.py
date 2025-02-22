from utils.mp3 import is_id3v1, is_id3v2, get_frames_from_id3v2, parse_frames_v1_2, parse_frames_v4, parse_frames_v3
import os


def read_mp3(fp):
    with (open(fp, "rb") as f):
        if is_id3v2(f):
            [frames, version] = get_frames_from_id3v2(f)
            print(frames)

            if version == 1 or version == 2:
                title, author = parse_frames_v1_2(frames)
                return {"title": title if title is not None else 'Без названия',
                        "author": author if author is not None else 'Автор не найден'}

            elif version == 3:
                title, author = parse_frames_v3(frames)
                return {"title": title if title is not None else 'Без названия',
                        "author": author if author is not None else 'Автор не найден'}

            elif version == 4:
                title, author = parse_frames_v4(frames)
                return {"title": title if title is not None else 'Без названия',
                        "author": author if author is not None else 'Автор не найден'}

        elif is_id3v1(f):  # первая версия тега
            f.seek(-128, 2)
            tag_data = f.read(128)

            title = tag_data[3:33].decode("latin-1").strip("\x00")
            artist = tag_data[33:63].decode("latin-1").strip("\x00")

            return {"title": title, "author": artist}

        else:
            file_name = os.path.basename(fp)
            return {"title": file_name.split('.')[0], "author": 'Автор не указан'}
