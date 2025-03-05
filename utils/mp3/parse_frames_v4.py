from utils.mp3 import get_syncsafe_size
from utils.mp3.decoding_info import decoding_info


def parse_frames_v4(frames):
    title_index = frames.find(b"TIT2")
    author_index = frames.find(b"TPE1")

    title = None
    author = None

    print(frames)

    if author_index != -1:
        author_size = get_syncsafe_size(frames[author_index + 4: author_index + 8])
        print('автор размер ',author_size)
        author_bytes = frames[
                       author_index + 10:
                       author_index + 10 + author_size
                       ]
        print('байты автора ',author_bytes)
        author = decoding_info(author_bytes)

    if title_index != -1:
        title_size = get_syncsafe_size(frames[title_index + 4: title_index + 8])
        print('размер титле ',title_size)
        title_bytes = frames[
                      # id(4) + размер(4) + флаги(2) = 10
                      # id(4) + размер(4) + флаги(2)+ размер тега = 10 + размер тега
                      title_index + 10:
                      title_index + 10 + title_size
                      ]
        print('байты титле ',title_bytes)
        title = decoding_info(title_bytes)

    return [title, author]
