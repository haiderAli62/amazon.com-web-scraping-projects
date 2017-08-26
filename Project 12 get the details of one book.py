from selenium import webdriver

from bs4 import BeautifulSoup
#import requests

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1502258079&sr=8-1&keywords=python+programming"
driver.get(url)
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')

table = bsObj.find("table" , {"id":"productDetailsTable"})
all_li = table.find_all("li")
isbn = all_li[3].text.strip("ISBN-10: ")
print(isbn)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
soup = BeautifulSoup(driver.page_source , "lxml")
description = soup.find("div").text

print(description)

driver.quit()



