from bs4 import BeautifulSoup as bs

from config import PATH, URL_AVITO

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def find_goods():
    service = Service(executable_path=PATH)
    print("### START PROCESS ###")
    driver = webdriver.Chrome(service=service)
    driver.get(URL_AVITO)
    page_data = driver.page_source
    soup = bs(page_data, "lxml")
    data = soup.find("div", class_="iva-item-title-py3i_")
    goods = data.find("a", class_="styles-module-root-QmppR")
    return ("avito.ru" + goods.get("href"))
