def get_syncsafe_size(bts):
    res = 0
    for byte in bts:
        res = res << 7 | (byte & 0x7F)

    return res

