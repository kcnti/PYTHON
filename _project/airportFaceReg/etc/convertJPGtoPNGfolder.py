import sys, os
from PIL import Image

first = sys.argv[1] #must have /
second = sys.argv[2] #must have /

if not os.path.exists(second):
	os.makedirs(second)

for filename in os.listdir(first):
	img = Image.open(f'{first}{filename}')
	splitName = os.path.splitext(filename)[0] #(('aaa', '.jpg'))
	img.save(f'{second}{splitName}.png', 'png')
print('done')