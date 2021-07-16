def make_readable(seconds):
    # Do something
    m, s = divmod(seconds, 60) # (หาร, เศษ)
    h, m = divmod(m, 60)
    return f'{h:02d}:{m:02d}:{s:02d}'

def make_readable2(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds / 3600, seconds / 60 % 60, seconds % 60)