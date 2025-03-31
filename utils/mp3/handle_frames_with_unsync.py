def handle_frames_with_unsync(uncleaned_frames: bytes, clear_size: int) -> bytes:
    clear_frames = bytearray()

    i = 0
    while len(clear_frames) < clear_size and i < len(uncleaned_frames):
        if i + 1 < len(uncleaned_frames) and uncleaned_frames[i] == 0xFF and uncleaned_frames[i + 1] == 0x00:
            clear_frames.append(uncleaned_frames[i])
            i += 2
        else:
            clear_frames.append(uncleaned_frames[i])
            i += 1

    return bytes(clear_frames)


