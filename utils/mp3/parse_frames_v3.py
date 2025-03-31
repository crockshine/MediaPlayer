from utils.mp3.decoding_info import decoding_info


def parse_frames_v3(frames: bytes, frame_id: bytes) -> None | str:
    """
        :param frames: все фреймы
        :param frame_id: ID необходимого фрейма
        :return: поиск и полученние информации из конкретного фрейма по его ID или None
    """
    frame_index = frames.find(frame_id)
    header = frames[frame_index : frame_index + 10]
    print('header frame v3', header)

    payload = None

    if frame_index != -1:
        # есть место для заголовка
        if len(frames) < frame_index + 10:
            return None

        size = int.from_bytes(header[4:8], 'big')
        flags = header[8:10]
        START_FRAME_DATA = frame_index + 10

        # есть ли место для данных
        if len(frames) < START_FRAME_DATA + size:
            return None

        frame_data = frames[START_FRAME_DATA : START_FRAME_DATA + size]
        print('frame_data', frame_data)

        compressed = bool(flags[1] & 0b00001000 != 0)
        encryption = bool(flags[1] & 0b00000100 != 0)
        group = bool(flags[1] & 0b00000010 != 0)

        print('compressed', compressed)
        print('group', group)

        if not encryption:
            offset = 0
            uncompressed_size = 0

            if compressed:
                if len(frame_data) < 4: return None
                uncompressed_size = int.from_bytes(frame_data[ : 4], 'big')
                offset += 4

            if group:
                if len(frame_data) <= offset: return None
                offset += 1

            if compressed:
                import zlib
                compressed_data = frame_data[offset : size]

                try:
                    decompressed_data = zlib.decompress(compressed_data)
                    if len(decompressed_data) != uncompressed_size: return None
                    payload = decoding_info(decompressed_data)
                except zlib.error:
                    payload = None
            else:
                payload = decoding_info(frame_data[offset : ])

    return payload
