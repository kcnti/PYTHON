def reverse(d):
    return {value: key for key,value in d.items()}

def keys(d, v):
    return list({key: value for key, value in d.items() if value == v})

exec(input().strip())
