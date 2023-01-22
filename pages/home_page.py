
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.themoviedb.org/?language=en'
        self.movies_locator = (
            By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/ul/li[1]/a')
        self.tv_shows_locator = (
            By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/ul/li[2]/a')

    def home_page(self):
        self.driver.get(self.url)

    def movies(self, option='Popular'):
        """
        Go to movie page depending on the option.
        Popular option is set by default.

        Keyword arguments:
        option - "Popular", "Now Playing", "Upcoming", "Top Rated"
        """

        driver = self.driver
        movies_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                self.movies_locator
            )
        )
        movies_button.click()
        movies_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, option)
            )
        )
        movies_option.click()

    def tv_shows(self, option='Popular'):
        """
        Go to tv show page depending on the option.
        Popular option is set by default.

        Keyword arguments:
        option - "Popular", "Airing Today", "On TV", "Top Rated"
        """
        driver = self.driver
        tv_shows_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                self.tv_shows_locator
            )
        )
        tv_shows_button.click()
        tv_shows_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, option)
            )
        )
        tv_shows_option.click()
