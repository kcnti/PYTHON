import requests
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
	return res

def getPwdLeaks(hashes, hash2check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash2check:
			return count
	return 0

def pwned_api_check(password):
	#print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper()) #unicode must be encoded before hash
	sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
	char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(char)
	#print(response)
	return getPwdLeaks(response, tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times')
		else:
			print(f'{password} was not found.')
	return 'done!'
#request_api_data('123')
if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
