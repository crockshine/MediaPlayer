from .get_syncsafe_size import get_syncsafe_size
from utils.mp3.handle_frames_with_unsync import handle_frames_with_unsync


def get_frames_from_id3v2(fb) -> [None | bytes, int]:
    """
    :param fb: filebytes
    :return: кортеж: frames - None | bytes, version - int | -1
    извлекает фреймы из файла, при необходимости обрабатывает Unsync
    """
    fb.seek(0, 0)
    tag_head_bytes = fb.read(10)

    if len(tag_head_bytes) < 10 or tag_head_bytes[:3] != b'ID3':
        return [None, -1]

    version_byte = tag_head_bytes[3]

    flag_byte = tag_head_bytes[5]
    unsync = flag_byte & 0b10000000 != 0

    # Проверка на компресcию во 2 версии
    # Проверка на лишние флаги
    if version_byte == 2 and flag_byte & 0b01000000 != 0 or flag_byte & 0b00011111 != 0:
        return [None, version_byte]

    frame_size = get_syncsafe_size(tag_head_bytes[6:10])
    frames: None | bytes = None
    fb.seek(10, 0)
    print('frames', frames)

    if unsync:
        print('опа ансинк')
        frames = handle_frames_with_unsync(fb.read(), frame_size)
    else:
        print('нету ансинк')
        frames = fb.read(frame_size)

    return [frames, version_byte]
