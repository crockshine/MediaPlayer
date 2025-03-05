from utils.mp3.decoding_info import decoding_info


def parse_frames_v1_2(frames):
    title_index = frames.find(b"TT2")
    author_index = frames.find(b"TP1")

    title = None
    author = None

    if title_index != -1:
        title_size = int.from_bytes(frames[title_index + 3: title_index + 6], 'big')
        title_bytes = frames[
                      title_index + 6:
                      title_index + 6 + title_size
                      ]

        title = decoding_info(title_bytes)

    if author_index != -1:
        author_size = int.from_bytes(frames[author_index + 3: author_index + 6], 'big')
        author_bytes = frames[
                       author_index + 6:
                       author_index + 6 + author_size
                       ]

        author = decoding_info(author_bytes)

    return [title, author]
