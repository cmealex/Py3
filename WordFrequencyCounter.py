import requests
from bs4 import BeautifulSoup as BS
import operator


def create_dictionary(clean_word_list):
    wc = {}
    for w in clean_word_list:
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1
    for k, v in sorted(wc.items(), key=operator.itemgetter(1)):  # sort by value
        print(k, v)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "all_symbols"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def start(url):
    word_list = []
    sc = requests.get(url).text
    soup = BS(sc)
    for pt in soup.find_all('a', {'class': 'xxx'}):
        content = pt.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)


start("url")
