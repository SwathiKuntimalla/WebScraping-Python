
import requests
import json
from bs4 import BeautifulSoup

import spacy
from spacy import displacy

web_url = input("Enter the Web Url:")


def retrieve_named_entities(web_url):
    NER = spacy.load("en_core_web_sm")
    source = requests.get(web_url)
    soup = BeautifulSoup(source.text, "html.parser")

    for para in soup.find_all('p'):
        t1 = NER(para.prettify())
        for word in t1.ents:
            print(f"text-{word.text}, label-{word.label_}")

retrieve_named_entities(web_url)


