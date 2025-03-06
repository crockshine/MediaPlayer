def handle_frames_with_unsync(frames):
    new_data = bytearray()

    if len(frames) > 0:
        i = 0
        while i < len(frames) - 1:
            if not (frames[i] == 0x00 and frames[i + 1] == 0xFF):
                new_data.append(frames[i])
            i += 1
        new_data.append(frames[-1])
    print(new_data, 'dasdasdasdasdasd')

    return new_data
