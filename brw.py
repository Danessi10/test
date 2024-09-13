from selenium import webdriver

class Browser:
    driver = webdriver.Chrome()

    @classmethod
    def load_page(cls, url):
        cls.driver.get(url)

    @classmethod
    def close_page(cls):
        cls.driver.quit()