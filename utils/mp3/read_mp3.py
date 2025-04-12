import os

from utils.mp3 import (
    is_id3v1,
    is_id3v2,
    get_frames_from_id3v2,
    parse_frames_v1_2,
    parse_frames_v4,
    parse_frames_v3
)


def read_mp3(fp):
    with (open(fp, "rb") as f):
        title = None
        author = None

        if is_id3v2(f):
            [frames, version] = get_frames_from_id3v2(f)

            if frames is not None:
                if version == 1 or version == 2:
                    title = parse_frames_v1_2(frames, b"TT2")
                    author = parse_frames_v1_2(frames, b"TP1")

                elif version == 3:
                    title = parse_frames_v3(frames, b"TIT2")
                    author = parse_frames_v3(frames, b"TPE1")

                elif version == 4:
                    [title, author] = parse_frames_v4(frames)

        elif is_id3v1(f):
            f.seek(-128, 2)
            tag_data = f.read(128)

            title = tag_data[3:33].decode("latin-1").strip("\x00")
            author = tag_data[33:63].decode("latin-1").strip("\x00")

        return {
            "title": title,
            "author": author
        }
