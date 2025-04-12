from utils.mp3.decoding_info import decoding_info


def parse_frames_v1_2(frames: bytes, frame_id: bytes) -> None | str:
    """
    :param frames: все фреймы
    :param frame_id: ID необходимого фрейма
    :return: поиск и полученние информации из конкретного фрейма по его ID или None
    """
    frame_index = frames.find(frame_id)
    payload = None

    if frame_index != -1:
        # есть место для заголовка
        if len(frames) < frame_index + 6: return None
        header = frames[frame_index: frame_index + 6]

        size = int.from_bytes(header[3 : 6], 'big')
        START_FRAME_DATA = frame_index + 6

        # есть ли место для данных
        if len(frames) < START_FRAME_DATA + size:
            return None

        if size >= 1:
            payload_bytes = frames[START_FRAME_DATA : START_FRAME_DATA + size]
            payload = decoding_info(payload_bytes)

    return payload
