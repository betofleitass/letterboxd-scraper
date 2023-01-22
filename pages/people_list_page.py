
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PeoplePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.themoviedb.org/person/?language=en'
        self.people_locator = (
            By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/ul/li[3]/a')
        self.names_locator = (
            By.XPATH, '//div/div/div/div/div/div/div[2]/p[1]/a')
        self.popular_by_locator = (
            By.XPATH, '//div/div/div/div/div/div/div[2]/p[2]')

    def open_page(self, option="Popular People"):
        """
        Returns a list of dictionarys
        with the information about the popular people.

        Limit the amount with the number parameter.

        Return:
        people (list)
        """
        driver = self.driver
        self.driver.get(self.url)

        people_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                self.people_locator
            )
        )
        people_button.click()
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
