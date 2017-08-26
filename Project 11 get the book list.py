from selenium import webdriver

from bs4 import BeautifulSoup
#import requests

class Book():
    def __init__(self):
        self.title = ""
        self.link = ""



def books_info():
    
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    url = "https://www.amazon.com/s/ref=nb_sb_noss/136-8911657-3180144?url=search-alias%3Daps&field-keywords=python+programming"
    driver.get(url)
    html_text = driver.page_source
    bsObj = BeautifulSoup(html_text , 'lxml')

    ul = bsObj.find("ul" , {"id":"s-results-list-atf"})
    book_list = []
    for li in ul.find_all("li" , class_ = "s-result-item celwidget "):
        a_tags = li.find_all("a")
        new_book = Book()
        new_book.title = a_tags[1].text
        new_book.link = a_tags[1]["href"]
        book_list.append(new_book)
        #print(a_tags[1].text)
        #print(a_tags[1]["href"])



    
    driver.quit()
    return book_list

#books_info()

b =books_info()

for book in b:
    print(book.title)
    print(book.link)



    




