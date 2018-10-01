import urllib2
from bs4 import BeautifulSoup
articleURL="https://www.washingtonpost.com/entertainment/books/for-kids-books-that-explore-immigration-war-and-other-thorny-issues/2018/09/11/a39efe50-b5f1-11e8-a2c5-3187f427e253_story.html?utm_term=.f00f587dc9f9"
#articleURL="https://profile.telugumatrimony.com/profiledetail/viewprofile.php?id=T3197630&tagid=&gaact=VP&gasrc=PINNABLELALL&osa=sphxos&actStatus=%2516Z%2508%2528%2500%2500Y%257B%252Fb%2522D%2514&srchTimeStmp=h%2501Wv_UN%2500vw&rand=&rlang=en"

page=urllib2.urlopen(articleURL).read().decode('utf8','ignore')
soup=BeautifulSoup(page,"lxml")
#print soup
str=soup.find('article')
#print str


str1=soup.find('article').text
#print str1

text=' '.join(map(lambda p:p.text, soup.find_all('article')))
print text