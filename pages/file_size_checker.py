
def bt_to_mb_conv(size):
    y = 2**10
    n = 0
    while size > y:
        size /= y
        n += 1
    return str(round(size, 2))
