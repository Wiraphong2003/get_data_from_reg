import requests
from bs4 import  BeautifulSoup

url = "https://www.sfcinemacity.com/movies"
webdata = requests.get(url)
print(webdata)
soup = BeautifulSoup(webdata.text,'html.parser')
print(soup)
find_word = soup.find_all("div",{"class":"movie-card flex-item"})
for i in find_word:
    print(i)

# find_word = soup.find_all('')