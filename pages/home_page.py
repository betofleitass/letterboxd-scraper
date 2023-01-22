
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
        self.people_locator = (
            By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/ul/li[3]/a')
        self.content_locator = (
            By.XPATH, '//div[@class="card style_1"]//div[@class="content"]')
        self.titles_locator = (
            By.XPATH, '//div/div[2]/h2/a')
        self.release_dates_locator = (
            By.XPATH, '//div/div[2]/p')
        self.user_scores_locator = (
            By.XPATH, '//div[@class="page_wrapper"]/div/div[2]/div/div/div/div/span')
        self.names_locator = (
            By.XPATH, '//div/div/div/div/div/div/div[2]/p[1]/a')
        self.popular_by_locator = (
            By.XPATH, '//div/div/div/div/div/div/div[2]/p[2]')

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

    def people(self, option="Popular People"):
        """
        Go to people page.
        """
        driver = self.driver
        people = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                self.people_locator
            )
        )
        people.click()
        people_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, option)
            )
        )
        people_option.click()

    def get_names(self):
        """
        Returns a list of the names
        """
        driver = self.driver
        names = WebDriverWait(driver, 10).until(
            EC.visibility_of_any_elements_located(
                self.names_locator
            )
        )

        return [element.text for element in names]

    def get_popular_by(self):
        """
        Returns a list of the popular by
        """
        driver = self.driver
        popular_by = WebDriverWait(driver, 10).until(
            EC.visibility_of_any_elements_located(
                self.popular_by_locator
            )
        )

        return [element.text.encode("utf-8").decode('ascii', 'ignore') for element in popular_by]

    def get_people_info(self, number=20):
        """
        Returns a list of dictionarys 
        with the information about the popular people.

        Limit the amount with the number parameter.

        Keyword arguments:
        number - A integer between 1 and 20

        Return:
        people (list)
        """
        names = self.get_names()
        popular_by = self.get_popular_by()

        people = []

        for i in range(number):
            people.append(
                {
                    "name": names[i],
                    "popular_by": popular_by[i],
                }
            )

        print(people)

        return people[:number]

    def get_content(self, number=20):
        """
        Returns a list of dictionarys 
        with the information about the movies or tv shows.

        Limit the amount with the number parameter.

        Keyword arguments:
        number - A integer between 1 and 20

        Return:
        content_list (list)
        """
        driver = self.driver
        content_list = []

        content = WebDriverWait(driver, 10).until(
            EC.visibility_of_any_elements_located(
                self.content_locator
            )
        )

        for element in content:

            title = element.find_element(By.XPATH, "./h2").text or "No title"
            release_date = element.find_element(
                By.XPATH, "./p").text or "No release date"
            user_score = element.find_element(
                By.XPATH, "./div/div/div").get_attribute("data-percent") or "No rated"

            content_list.append(
                {
                    "title": title,
                    "release_date": release_date,
                    "user_score": user_score
                }
            )

        return content_list
