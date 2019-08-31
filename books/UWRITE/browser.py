from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import os
import time

class SeleniumClass(object):
    def __init__(self, main_url, book_url):
        self.main_url = main_url
        self.book_url = book_url
        self.selenium()

    def selenium(self):

        #TODO Логика: проверяем на то, есть ли куки и валидные ли они, если нет - получаем новые
        driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__))+"/chromedriver")
        driver.get(self.main_url)
        time.sleep(1)

        try:
            #Закрываем всплывающее окно с предложением о какой-то фигне
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/button")
            button.click()
            time.sleep(1)
        except:
            pass

        #Заполнение логина/пароля на формах
        login_element = driver.find_element_by_xpath('//*[@id="login"]')
        login_element.click()
        login_element.clear()
        login_element.send_keys("ЛОГИН_БЛАТНОЙ")
        password_element = driver.find_element_by_xpath('//*[@id="password"]')
        password_element.click()
        password_element.clear()
        password_element.send_keys("ПАРОЛЬ_ТОЖЕ_БЛАТНОЙ")
        time.sleep(1)

        #Вход на сайт
        button = driver.find_element_by_xpath('//*[@id="button1id"]')
        button.click()
        driver.get(self.book_url)
        cookies = driver.get_cookies()
        print(cookies)