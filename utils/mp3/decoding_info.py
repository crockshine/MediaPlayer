def decoding_info(info_bytes: bytes):
    if not info_bytes:
        return None

    encoding = info_bytes[0]
    text_bytes = info_bytes[1:]

    try:
        if encoding == 0x00:
            decoded_text = text_bytes.split(b'\x00', 1)[0].decode('latin-1')
            return decoded_text if len(decoded_text) > 0 else None

        elif encoding == 0x01:
            if len(text_bytes) % 2 != 0:
                return None
            decoded_text = text_bytes.split(b'\x00\x00', 1)[0].decode('utf-16')
            return decoded_text if len(decoded_text) > 0 else None

        elif encoding == 0x02:
            if len(text_bytes) % 2 != 0:
                return None
            decoded_text = text_bytes.split(b'\x00\x00', 1)[0].decode('utf-16-be')
            return decoded_text if len(decoded_text) > 0 else None

        elif encoding == 0x03:
            decoded_text = text_bytes.split(b'\x00', 1)[0].decode('utf-8')
            return decoded_text if len(decoded_text) > 0 else None

        else:
            decoded_text = text_bytes.decode('latin-1')
            return decoded_text if len(decoded_text) > 0 else None
    except UnicodeDecodeError:
        return None #обработка ошибок