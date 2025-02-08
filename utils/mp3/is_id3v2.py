def is_id3v2(fp):
    fp.seek(128, 0)
    tag_data = fp.read(128)

    if tag_data[:3] == b"TAG": # Проверяем, есть ли ID3v2
        return True
