from bs4 import BeautifulSoup
import urllib
import mechanize

base_url = "http://www.securitytube.net/video/3000"

httpResponse = urllib.urlopen(base_url)
print httpResponse.code
html = httpResponse.read()
print html
bt = BeautifulSoup(html, 'lxml')


