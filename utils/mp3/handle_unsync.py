def handle_unsync(uncleaned_data: bytes, clear_size: int) -> bytes:
    clear_frames = bytearray()
    i = 0
    n = len(uncleaned_data)

    while len(clear_frames) < clear_size and i < n:
        if i + 2 < n and uncleaned_data[i] == 0xFF and uncleaned_data[i+1] == 0x00:
            if uncleaned_data[i+2] == 0x00:
                clear_frames.extend([0xFF, 0x00])
                i += 3
            elif (uncleaned_data[i+2] & 0xE0) == 0xE0 and uncleaned_data[i+2] != 0xFF:
                clear_frames.extend([0xFF, uncleaned_data[i+2]])
                i += 3
            else:
                clear_frames.append(uncleaned_data[i])
                i += 1
        else:
            clear_frames.append(uncleaned_data[i])
            i += 1

    return bytes(clear_frames[:clear_size])

