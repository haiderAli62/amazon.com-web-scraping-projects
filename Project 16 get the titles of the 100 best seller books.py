from selenium import webdriver

from bs4 import BeautifulSoup
#import requests


def get_book_pages():
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books#{0}"
    driver.get(url)
    html_text = driver.page_source
    bsObj = BeautifulSoup(html_text , 'lxml')
    
    pages_links = []
    div = bsObj.find("div" , {"id":"zg_paginationWrapper"})
    for li in div.find_all("a"):
        #print(li["href"]+"\n")
        pages_links.append(li["href"])

    
    
    return pages_links


def get_books_titles(books_links):
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    for book in books_links:
        url = book        
        driver.get(url)
        html_text = driver.page_source
        bsObj = BeautifulSoup(html_text , 'lxml')
        books_title = []
        div = bsObj.find("div" , {"id":"zg_left_col1"})
        for all_div in div.find_all("div" , class_ = "p13n-sc-truncated-hyphen p13n-sc-truncated"):
            print(all_div.text)
            books_title.append(all_div.text)
    
    return books_title
            
get_books_titles(get_book_pages())

            


