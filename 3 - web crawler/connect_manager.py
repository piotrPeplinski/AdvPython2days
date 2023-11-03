from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ConnectToSite:
    def __init__(self, url: str):
        self.url = url

    def __enter__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        return self.driver

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.driver.quit()
