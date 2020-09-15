import requests 
import re 

the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def get_book(url):
    # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Discards the metadata from the beginning of the book
    start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*",raw ).end()
    # Discards the text starting Part 2 of the book
    stop = re.search(r"II", raw).start()
    # Keeps the relevant text
    text = raw[start:stop]
    return text

def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower() 

def convert_i(text):
    return re.sub(r'\si\s', " I ", text)



book = get_book(the_idiot_url)
processed_book = preprocess(book)
print(len(re.findall(r'the', processed_book)))
print(convert_i(processed_book))
print(len(re.findall(r'\".+\"', processed_book))) #Number of quotations
