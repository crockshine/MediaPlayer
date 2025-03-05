from utils.mp3.decoding_info import decoding_info


def parse_frames_v3(frames):
    title_index = frames.find(b"TIT2")
    author_index = frames.find(b"TPE1")
    print(author_index)
    title = None
    author = None

    print(frames)

    if title_index != -1:
        title_size = int.from_bytes(
            frames[title_index + 4: title_index + 8], 'big'
        )

        print(title_size)

        title_bytes = frames[
                      # id(4) + размер(4) + флаги(2) = 10
                      # id(4) + размер(4) + флаги(2)+ размер тега = 10 + размер тега
                      title_index + 10:
                      title_index + 10 + title_size
                      ]
        title = decoding_info(title_bytes)

    if author_index != -1:
        author_size = int.from_bytes(frames[author_index + 4: author_index + 8], 'big')
        print(author_size, 'a size')
        author_bytes = frames[
                       author_index + 10:
                       author_index + 10 + author_size
                       ]
        author = decoding_info(author_bytes)

    return [title, author]
