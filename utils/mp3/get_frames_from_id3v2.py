from .get_syncsafe_size import get_syncsafe_size
from utils.mp3.handle_frames_with_unsync import handle_frames_with_unsync


def get_frames_from_id3v2(fb):
    def is_frame_id(data):
        res = False
        for byte in data:
            if 65 <= byte <= 90 or 48 <= byte <= 57:
                return True
            else:
                res = False
        return res

    fb.seek(0, 0)

    tag_head_bytes = fb.read(10)
    version_byte = tag_head_bytes[3]
    flag_byte = tag_head_bytes[5]
    flags = {
        "Unsync": bool(flag_byte & 0b10000000 != 0),
        "Extended header": bool(False)
        # расширеный заголвоок далее определяется по 4 байтам после основного заголовка
    }
    frame_size = get_syncsafe_size(tag_head_bytes[6:10])
    print(tag_head_bytes[6:10])

    frames = None

    # проверка на расширеный заголовок. 3 версия - bigint, 4 - syncsafe
    fb.seek(10)
    extended_bytes = fb.read(4)
    if not is_frame_id(extended_bytes):  # наткнулись на расширенный заголовок
        flags["Extended header"] = True
        extended_size = 0

        if version_byte == 3:
            extended_size = int.from_bytes(extended_bytes, 'big')
        if version_byte == 4:
            extended_size = get_syncsafe_size(extended_bytes)

        fb.seek(10 + 4 + extended_size)
        frames = fb.read(frame_size - extended_size)
    else:
        fb.seek(10)
        frames = fb.read(frame_size)

    if flags["Unsync"] and len(frames) > 0:
        frames = handle_frames_with_unsync(frames)
    else:
        if not flags["Extended header"]:
            fb.seek(10)
            frames = fb.read(frame_size)

    return [frames, version_byte]
