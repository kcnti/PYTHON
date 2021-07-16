def to_jaden_case(string):
    quote = ' '.join([s[0].upper() + s[1:] for s in string.split(' ')])
    return quote