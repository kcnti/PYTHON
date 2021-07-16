from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil

one = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//1//"
two = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//2//"
three = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//3//"
four = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//4//"
five = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//5//"
six = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//6//"
seven ="D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//7//"
eight = "D://__PROJ//_WORK//coding//python//_project//scrapingImage//photo//8//"

img_info = []
r = requests.get('http://e-psm.net:8091/files/upload/202007/CJ9B194760004/')
soup = BeautifulSoup(r.text, 'html.parser')
img = soup.find_all("a")
for i in img:
    img_info.append(i['href'])
    for _ in img_info:
        if not _.startswith("2"):
            img_info.remove(_)
print(img_info)

def download(image):
    #print(image[0])
    r = requests.get("http://e-psm.net:8091/files/upload/202007/CJ9B194760004/"+image, stream=True)
    #name = ''.join(_ for _ in image[1] if _.isalnum())
    # print(name)
    _file = open(f'{one}{image}.jpg', 'wb')
    r.raw.decode_content = True
    shutil.copyfileobj(r.raw, _file)
    del r

for i in range(0, len(img_info)):
    print(img_info[i])
    download(img_info[i])