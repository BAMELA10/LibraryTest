from .TestPage import TestPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ExceptionTestPage(TestPage):
    """
    A class to represent a test page for handling exceptions using Selenium WebDriver.
    This class provides methods to check for various exceptions that may occur during web interactions.
    It uses the Firefox WebDriver to interact with the web page.
    """
    def __init__(self, base_url, url,input_text=None):
        """
        Initializes the ExceptionTestPage with a base URL and specific URL.
        Args:
            base_url (str): The base URL of the website.
            url (str): The specific URL for the test page.
            input_text (str): The text to be used in input fields during tests.
        """
        # Initialize the parent class with the base URL and specific URL
        super().__init__(base_url, url)
        self.input_text = input_text

    def check_NoSuchElementException(self, xpath_add_button, xpath_row2):
        """
        Checks for NoSuchElementException by attempting to find an element that does not exist.
        Args:
            xpath_add_button (str): The XPath of the add button.
            xpath_row2 (str): The XPath of the second row element.
        Returns:
            None
        Raises:
            NoSuchElementException: If the element is not found.
        """
        driver = self.driver
        driver.get(self.final_url)
        driver.find_element(By.XPATH, xpath_add_button).click()
        driver.find_element(By.XPATH, xpath_row2)

    def check_ElementNotInteractableException(self, xpath_add_button, xpath_row2, xpath_input_row2, id_confirmation, name_save_button):
        """
        Checks for ElementNotInteractableException by attempting to interact with an element that is not interactable.
        Args:
            xpath_add_button (str): The XPath of the add button.
            xpath_row2 (str): The XPath of the second row element.
            xpath_input_row2 (str): The XPath of the input field in the second row.
            id_confirmation (str): The ID of the confirmation element.
            name_save_button (str): The name of the save button.
        Returns:
            None
        Raises:
            ElementNotInteractableException: If the element is not interactable.
        """
        driver = self.driver
        driver.get(self.final_url)
        driver.find_element(By.XPATH, xpath_add_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_row2)))
        driver.find_element(By.XPATH, xpath_input_row2).send_keys(self.input_text)
        driver.find_element(By.NAME, name_save_button).click()
        driver.find_element(By.ID, id_confirmation).click()


    def check_InvalidElementStateException(self, confirmation_message, id_edit_button, xpath_input_row1, xpath_save_button):
        """
        Checks for InvalidElementStateException by attempting to interact with an element in an invalid state.
        Args:
            confirmation_message (str): The message to confirm successful interaction.
            id_edit_button (str): The ID of the edit button.
            xpath_input_row1 (str): The XPath of the input field in the first row.
            xpath_save_button (str): The XPath of the save button.
        Returns:
            None
        Raises:
            InvalidElementStateException: If the element is in an invalid state.
        """
        driver = self.driver
        driver.get(self.final_url)
        driver.find_element(By.XPATH, xpath_input_row1).clear()
        driver.find_element(By.XPATH, xpath_input_row1).send_keys(self.input_text)
        driver.find_element(By.XPATH, xpath_save_button).click()
        if not confirmation_message in driver.page_source:
            raise AssertionError(f"confirmation message '{confirmation_message}' not found in page source.")



    def check_StaleElementReferenceException(self, id_instruction, xpath_add_button):
        """
        Checks for StaleElementReferenceException by attempting to interact with a stale element.
        Args:
            id_instruction (str): The ID of the instruction element.
            xpath_add_button (str): The XPath of the add button.
        Returns:
            None
        Raises:
            StaleElementReferenceException: If the element is stale.
        """
        driver = self.driver
        driver.get(self.final_url)
        instruction_elt = driver.find_element(By.ID, id_instruction)
        driver.find_element(By.XPATH, xpath_add_button).click()
        var = instruction_elt.is_displayed()

    def check_TimeoutException(self, xpath_add_button, xpath_input_row2):
        """
        Checks for TimeoutException by attempting to find an element that takes too long to load.
        Args:
            xpath_add_button (str): The XPath of the add button.
            xpath_input_row2 (str): The XPath of the input field in the second row.
        Returns:
            None
        Raises:
            TimeoutException: If the element takes too long to load.
        """
        driver = self.driver
        driver.get(self.final_url)
        driver.find_element(By.XPATH, xpath_add_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_input_row2)))
