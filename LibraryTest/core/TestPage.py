from selenium import webdriver
class TestPage:
    def __init__(self, base_url, url):
        self.driver = webdriver.Firefox()
        self.base_url = base_url
        self.url = url
        self.final_url = self.base_url + self.url
        