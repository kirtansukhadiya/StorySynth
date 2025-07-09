from proxy import *
from bs4 import BeautifulSoup #for webscrapping
import requests 
from openai import OpenAI #for chatGPT
import openai
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def book_name(): 
    try:    #if the book name matches to any book in the website this block will get run
        print("This results are from website Goodreads")
        url_Book_Name = (str(Book_Name.replace(' ','+'))) #for making url
        url = ("https://www.goodreads.com/search?utf8=✓&q="+url_Book_Name+"&search_type=books") #creating url
        #print(url)
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.content, 'lxml')
        book = soup.find('a', class_ = 'bookTitle').text.replace('\n','')
        author_name = soup.find('a', class_ = "authorName").text
        rating_of_book = soup.find('span', class_ = "minirating").text.replace('—',"which is average of")
        publish_date = soup.find('span', class_="greyText smallText uitext")#replace('\n','').replace(' ','',14) #parent
        publish_date.span.clear()
        publish_date.a.clear()
        publish_date_text = (publish_date).text.replace('\n','').replace('—','').replace("                              published","Pulished in:- ").replace('               ',' ')
        print("Name:- "+book) 
        print("Author's Name:- "+author_name)
        print("Rating of the book out of 5:- "+rating_of_book)
        print(publish_date_text)

    except AttributeError: #if there is no book of the same name of book on website the program will start again using this block of code
        print("No book found:)\nPlease re-enter the name with corret spelling")
        book_info_needed()
        book_name()

secret_key = openai.api_key = str(os.getenv("OPENAI_API_KEY")) #setting the secret key for openai api

def Summary(x):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": f"Give a short summary of the book '{x}'."}
        ]
    )
    print("Summary:", response.choices[0].message.content)

def book_info_needed():
    global Book_Name, options
    Book_Name = input("Enter the book name: ")
    Book_Name = Book_Name.lower()
    options = input("What output do you desire?\n1. Details\n2. Summary\n=> ").strip().lower()

    if options == "1" or options == "details":
        book_name()
    elif options == "2" or options == "summary":
        Summary(Book_Name)
    else:
        print("Invalid option. Please enter '1' or '2'.")

book_info_needed() #starts the program
