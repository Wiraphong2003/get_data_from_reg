import requests
from bs4 import  BeautifulSoup

url = "http://reg.msu.ac.th/registrar/class_info_1.asp?avs792046395=17&backto=home"
webdata = requests.get(url)
print(webdata)
soup = BeautifulSoup(webdata.text,'html.parser')
find_word = soup.find_all("table",{"class":"normalDetail"})
for i in find_word:
    print(i)

# find_word = soup.find_all('')