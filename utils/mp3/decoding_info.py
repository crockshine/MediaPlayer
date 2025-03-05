def decoding_info(info_bytes: bytes):
    encoding = info_bytes[0]
    text_bytes = info_bytes[1:]
    if encoding == 0x00:
        return text_bytes.split(b'\x00', 1)[0].decode('latin-1')
    elif encoding == 0x01:
        return text_bytes.split(b'\x00\x00', 1)[0].decode('utf-16')
    elif encoding == 0x02:
        return text_bytes.split(b'\x00\x00', 1)[0].decode('utf-16-be')
    elif encoding == 0x03:
        return text_bytes.split(b'\x00', 1)[0].decode('utf-8')
    else:
        return text_bytes.decode('latin-1', errors='replace')