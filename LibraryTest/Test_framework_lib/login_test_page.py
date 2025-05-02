from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginTestPage:
    """
    A class to represent a login test page using Selenium WebDriver.
    this class provides methods to perform positive and negative login tests.
    It uses the Firefox WebDriver to interact with the web page.

    Attributes:
    
            driver (webdriver): The Selenium WebDriver instance.
            base_url (str): The base URL of the website.
            url (str): The specific URL for the login page.
            login_url (str): The full URL for the login page.
    Methods:
    
            postive_login_test(username, password, xpath_username, xpath_password, xpath_login_button,xpath_logout_button, login_url, confirmation_message):
                Performs a positive login test.
            invalid_credentials_test(username, password, xpath_username, xpath_password, xpath_login_button,xpath_error_message_box,error_message):
                Performs a negative login test with invalid credentials.
    
    """
    def __init__(self, base_url, url):
        self.driver = webdriver.Firefox()
        self.base_url = base_url
        self.url = url
        self.login_url = self.base_url + self.url
        

    def postive_login_test(self, username, password, xpath_username, xpath_password, xpath_login_button,xpath_logout_button, login_url, confirmation_message):
        """
        Performs a positive login test.
        Args:
            username (str): The username to use for login.
            password (str): The password to use for login.
            xpath_username (str): The XPath of the username input field.
            xpath_password (str): The XPath of the password input field.
            xpath_login_button (str): The XPath of the login button.
            xpath_logout_button (str): The XPath of the logout button.
            login_url (str): The expected URL after successful login.
            confirmation_message (str): The message to confirm successful login.
        
        Returns:
            None
        Raises:
            AssertionError: If the login is not successful or the confirmation message is not found.
            NoSuchElementException: If the xpath of Dom element is not true.
        """
        driver = self.driver
        driver.get(self.login_url)
        driver.find_element(By.XPATH, xpath_username).send_keys(username)
        driver.find_element(By.XPATH, xpath_password).send_keys(password)
        driver.find_element(By.XPATH, xpath_login_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_url))
        assert driver.current_url == login_url, f"Expected URL: {login_url}, but got: {driver.current_url}"
        if not confirmation_message in driver.page_source:
            raise AssertionError(f"Confirmation message '{confirmation_message}' not found in page source.")
        var = driver.find_element(By.XPATH, xpath_logout_button).is_displayed()
        assert var, "Logout button is not displayed."
        driver.quit()
        print("Positive login test passed.")

    def invalid_credentials_test(self, username, password, xpath_username, xpath_password, xpath_login_button,xpath_error_message_box,error_message):
        """
        Performs a negative login test with invalid credentials.
        Args:
            username (str): The username to use for login.
            password (str): The password to use for login.
            xpath_username (str): The XPath of the username input field.
            xpath_password (str): The XPath of the password input field.
            xpath_login_button (str): The XPath of the login button.
            xpath_error_message_box (str): The XPath of the error message box.
            error_message (str): The expected error message for invalid credentials.
        Returns:
            None
        Raises:
            AssertionError: If the error message is not displayed or does not match the expected message.
            NoSuchElementException: If the xpath of Dom element is not true.
            
        
        """
        driver = self.driver
        driver.get(self.login_url)
        driver.find_element(By.XPATH, xpath_username).send_keys(username)
        driver.find_element(By.XPATH, xpath_password).send_keys(password)
        driver.find_element(By.XPATH, xpath_login_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_error_message_box)))
        var = driver.find_element(By.XPATH, xpath_error_message_box).is_displayed()
        assert var, "Error message is not displayed."
        if not error_message in driver.page_source:
            raise AssertionError(f"error message '{error_message}' not found in page source.")
        driver.quit()
        print("invalid credentials login test passed.")