def is_id3v2(fp):
    fp.seek(0, 0)
    tag_data = fp.read(3)
    print(tag_data)
    # [: 3].decode("latin-1")
    if tag_data[:3] == b"ID3": # Проверяем, есть ли ID3v2
        return True
    else:
        return False
