import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


class GetTVShowsTest(unittest.TestCase):

    # Decorator allows to different pages run in the same window
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(5)
        driver.maximize_window()

    def test_get_tv_shows(self):
        tmdb = HomePage(self.driver)
        tmdb.home_page()
        tmdb.tv_shows()
        tmdb.get_info()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reports/GetTVShowsTest',
        report_name='GetTVShowsTest_report',
        report_title='Get TV Shows Test')
    )
