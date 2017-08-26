from selenium import webdriver

from bs4 import BeautifulSoup
#import requests

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1502258079&sr=8-1&keywords=python+programming"
driver.get(url)
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')

div_1 = bsObj.find("div" , {"id":"cm-cr-dp-review-list"})
for span in div_1.find_all("span" , class_ = "a-size-base review-text"):
    print(span.text+"\n")




driver.quit()



