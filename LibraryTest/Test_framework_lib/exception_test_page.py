from selenium import webdriver

class ExceptionTestPage:
    def __init__(self,base_url, url):
        self.driver = webdriver.Firefox()
        self.base_url = base_url
        self.url = url
        self.login_url = self.base_url + self.url

    def check_NoSuchElementException(self):
        pass

    def check_ElementNotInteractableException(self):
        pass

    def check_InvalidElementStateException(self):
        pass

    def check_StaleElementReferenceException(self):
        pass

    def check_TimeoutException(self):
        pass