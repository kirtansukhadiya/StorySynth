from proxy import *
from bs4 import BeautifulSoup #for webscrapping
import requests 


def book_name(): 
    try:    #if the book name matches to any book in the website this block will get run
        url_Book_Name = (str(Book_Name.replace(' ','+'))) #for making url
        url = ("https://openlibrary.org/search?q="+url_Book_Name+"&mode=everything") #creating url
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.content, 'lxml')
        book = soup.find('h3', class_ = 'booktitle').text.replace('\n','')
        publish_date_span = soup.find('span', class_ = "resultDetails") #parent
        publish_date = publish_date_span.find('span').text.replace('\n','').replace(' ','',14) #child
        print(book) 
        print(publish_date)

    except AttributeError: #if there is no book of the same name of book on website the program will start again using this block of code
        book_info_needed()
        book_name()

def book_info_needed():
    global Book_Name, options
    Book_Name = input("Enter the book name: ", ) #Name of the book you want to know about
    options = input("What output do desire?\n1.Details\n=>") #what do you want to know about
    if options == "1" or "Details" or "details" :
        book_name()
    else:
        pass

book_info_needed() #starts the program