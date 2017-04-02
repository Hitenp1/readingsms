import requests
from bs4 import BeautifulSoup

def titlefinder(url):
  r = requests.get(url)
  r_html = r.text

  soup = BeautifulSoup(r_html, "lxml")
  title = [item['data-sharetitle'] for item in soup.find_all('li', attrs={'data-sharetitle' : True})]

  print("\n".join(title))

titlefinder('https://www.techcrunch.com/')
print("Page2")
titlefinder('https://techcrunch.com/page/2/')


#ganesha
