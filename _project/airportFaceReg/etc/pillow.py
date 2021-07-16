from PIL import Image, ImageFilter

img = Image.open('correct.jpg')
filteredImage = img.filter(ImageFilter.SHARPEN) #to blur, sharpen
filteredImage = img.convert('L') #to grayscale
_rotate = filteredImage.rotate(180) # rotate
_resize = _rotate.resize((1920, 1080)) # resize
_resize.save('blurr.png', 'png') #change to png
_resize.show()