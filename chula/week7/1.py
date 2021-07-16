_input = input()

if _input.endswith('s') or _input.endswith('x') or _input.endswith('ch'):
    _input+='es'
elif _input.endswith('y') and _input[len(_input)-2] not in 'aeiou':
    _input = _input[:-1]+'ies'
else:
    _input+='s'

print(_input)
