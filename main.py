import requests
from bs4 import BeautifulSoup

url = "http://reg.msu.ac.th/registrar/class_info_1.asp?avs792045499=19&backto=enroll"
webdata = requests.get(url)
print(webdata)
# soup = BeautifulSoup(webdata.text,'html.parser')
# find_word = soup.find_all('')