import time
import requests
from requests.api import request
import datetime

URL = "https://api.hh.ru"

def default_request(text, page=0):
    """Запрос к API HeadHunter'а"""
    r = requests.get(URL+"/vacancies?text={}&area=1&per_page=100&page={}".format(text, page)).json()
    return r

def vacancy_info_request():
    pass
    

def main():

    search_words  = ["Python" , "Java", "React"]
    for word in search_words:

        r = default_request(word)
        print("Всего вакансий со словом {}: {}".format(word, r["found"]))
        
        #for item in r["items"]:
        #    salary = item["salary"]
        #    requirement_words = item["snippet"]["requirement"]
        #    print(requirement_words)

if __name__ == "__main__":
    main()