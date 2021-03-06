from bs4 import BeautifulSoup
import requests
import sys

name = sys.argv[1]
url = requests.get(f"https://r6.tracker.network/profile/pc/{name}")
soup = BeautifulSoup(url.content, "html.parser")
#data = soup.find("h1").get_text()

ranked = soup.find("div", {"style":"flex-grow: 1; display: flex; justify-content: space-between; align-items: center;"})
#print(data.get_text('\n', strip=True))
win = soup.find('div', {'class':'trn-scont__content'})
print(win.get_text(' ', strip=True))

