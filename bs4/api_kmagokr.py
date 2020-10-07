import requests
from bs4 import BeautifulSoup

info_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
response = requests.get(info_url)
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())
locations = soup.find_all('location')
for location in locations:
  print(location.find('city').text, ":", location.find('wf').text)
