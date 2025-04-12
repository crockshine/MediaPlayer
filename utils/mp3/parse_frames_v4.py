import zlib

from utils.mp3 import get_syncsafe_size
from utils.mp3.decoding_info import decoding_info
from utils.mp3.handle_unsync import handle_frames_with_unsync


def handle_frame_with_flags(frame_data, flags):
    if bool(flags[1] & 0x01):
        return None

    if bool(flags[1] & 0x08):
        frame_data = handle_frames_with_unsync(frame_data)

    if bool(flags[1] & 0x02):
        if flags[1] & 0x04:  # Проверка Data Length Indicator (бит 2)
            compressed_data = frame_data[4:]
        else:
            compressed_data = frame_data

        try:
            frame_data = zlib.decompress(compressed_data)
        except zlib.error:
            return None

    return frame_data


def parse_frames_v4(frames: bytes, frame_id: bytes) -> None | str:
    """
           :param frames: все фреймы
           :param frame_id: ID необходимого фрейма
           :return: поиск и полученние информации из конкретного фрейма по его ID или None
    """

    frame_index = frames.find(frame_id)
    header = frames[frame_index: frame_index + 10]
    print('header frame v4', header)

    payload = None

    if frame_index != -1:
        size = get_syncsafe_size(frames[frame_index + 4: frame_index + 8])
        print('автор размер ', author_size)
        author_bytes = frames[
                       author_index + 10:
                       author_index + 10 + author_size + 1
                       ]
        print('байты автора до', author_bytes)
        author_bytes = handle_frame_with_flags(author_bytes, frames[author_index + 8: author_index + 10])
        print('байты автора после', author_bytes)
        author = decoding_info(author_bytes)

    if title_index != -1:
        title_size = get_syncsafe_size(frames[title_index + 4: title_index + 8])
        print('размер титле ', title_size)
        title_bytes = frames[
                      # id(4) + размер(4) + флаги(2) = 10
                      # id(4) + размер(4) + флаги(2)+ размер тега = 10 + размер тега
                      title_index + 10:
                      title_index + 10 + title_size + 1
                      ]
        print('байты титле до', title_bytes)
        title_bytes = handle_frame_with_flags(title_bytes, frames[title_index + 8: title_index + 10])
        print('байты титле после', title_bytes)
        title = decoding_info(title_bytes)

    return [title, author]
