def decoding_info(info_bytes: bytes):
    if not info_bytes:
        return None

    encoding = info_bytes[0]
    text_bytes = info_bytes[1:]

    try:
        if encoding == 0x00: #latin-1
            end = text_bytes.find(b'\x00')
            if end == -1: end = len(text_bytes)
            return text_bytes[:end].decode('latin-1')

        elif encoding == 0x01: #utf-16
            if len(text_bytes) < 2 or len(text_bytes) % 2 != 0:  return None

            end = text_bytes.find(b'\x00\x00')
            if end == -1: end = len(text_bytes)

            if text_bytes[:2] == b'\xFF\xFE':
                return text_bytes[2:end].decode('utf-16-le')
            elif text_bytes[:2] == b'\xFE\xFF':
                return text_bytes[:end].decode('utf-16-be')
            else:
                return text_bytes[:end].decode('utf-16-be')

        elif encoding == 0x03: #utf-8
            end = text_bytes.find(b'\x00')
            if end == -1: end = len(text_bytes)
            return text_bytes[:end].decode('utf-8')

        else:
            end = text_bytes.find(b'\x00')
            if end == -1: end = len(text_bytes)
            return text_bytes[:end].decode('latin-1')

    except UnicodeDecodeError:
        return None


