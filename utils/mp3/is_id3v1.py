def is_id3v1(fp):
    fp.seek(-128, 2)
    tag_data = fp.read(128)

    if tag_data[:3] == b"TAG": # Проверяем, есть ли ID3v1
        return True
