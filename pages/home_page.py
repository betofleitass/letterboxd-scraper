
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.themoviedb.org/'

    def home_page(self):
        self._driver.get(self._url)
