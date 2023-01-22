
class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.themoviedb.org/?language=en'

    def open_page(self):
        self.driver.get(self.url)
