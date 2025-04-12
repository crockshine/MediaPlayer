from .get_syncsafe_size import get_syncsafe_size
from utils.mp3.handle_unsync import handle_unsync


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
    revision = tag_head_bytes[4]

    flag_byte = tag_head_bytes[5]
    unsync = flag_byte & 0b10000000 != 0

    # При ревизии может быть непредсказуемый результат
    if revision != 0 : return [None, -1]

    # Проверка на компресcию во 2 версии
    # Проверка на лишние флаги
    if version_byte == 2 and flag_byte & 0b01000000 != 0 or flag_byte & 0b00111111 != 0:
        return [None, version_byte]

    if version_byte == 3 and flag_byte & 0b00011111 != 0:
        return [None, version_byte]

    if version_byte == 4 and flag_byte & 0b00001111 != 0:
        return [None, version_byte]


    frame_size = get_syncsafe_size(tag_head_bytes[6:10])
    fb.seek(10, 0)

    if unsync:
        print('опа ансинк')
        frames = handle_unsync(fb.read(), frame_size)
    else:
        print('нету ансинк')
        frames = fb.read(frame_size)
        if len(frames) < frame_size :
            return [None, version_byte]

    return [frames, version_byte]
