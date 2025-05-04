# LibraryTest - Selenium Automated Testing Framework

## Overview
LibraryTest is a Selenium WebDriver-based automated testing framework designed to facilitate testing of web applications with a focus on exception handling and login functionality. The framework provides reusable core classes to test common Selenium exceptions and perform login tests, along with organized test cases demonstrating their usage.

## Features
- Exception testing for common Selenium exceptions such as:
  - NoSuchElementException
  - ElementNotInteractableException
  - InvalidElementStateException
  - StaleElementReferenceException
  - TimeoutException
- Login testing with positive and negative test cases
- Uses Firefox WebDriver for browser automation
- Modular design with core classes and separate test case scripts

## Project Structure
```
LibraryTest/
├── core/                       # Core Selenium test classes
│   ├── exception_test_page.py  # Exception testing class
│   ├── login_test_page.py      # Login testing class
│   └── TestPage.py             # Base test page class
├── Test/                       # Test case scripts
│   ├── Exception_case/         # Exception test cases
│   └── login_case/             # Login test cases
├── requirement.txt             # Project dependencies
├── setup.py                   # Setup script for the project
└── readme.md                  # Project documentation
```

## Usage
1. Install the required dependencies (see Requirements section).
2. Configure the test parameters such as URLs, XPath selectors, usernames, and passwords in the test case scripts.
3. Run the test case scripts to execute the automated tests.

Example usage in a test case:
```python
from LibraryTest.core.exception_test_page import ExceptionTestPage

exception_page = ExceptionTestPage("https://practicetestautomation.com/", "practice-test-exceptions/", "test")
exception_page.check_ElementNotInteractableException(
    xpath_add_button='//*[@id="add_btn"]',
    xpath_row2='//*[@id="row2"]',
    xpath_input_row2='//*[@id="row2"]/input',
    id_confirmation='confirmation',
    name_save_button='Save'
)
```

## Requirements
- Python 3.x
- Selenium
- Firefox WebDriver (geckodriver)

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install Selenium:
   ```
   pip install selenium
   ```
3. Download and install Firefox WebDriver (geckodriver) from [Mozilla GitHub](https://github.com/mozilla/geckodriver/releases) and ensure it is in your system PATH.
4. Install other dependencies listed in `requirement.txt` if any:
   ```
   pip install -r requirement.txt
   ```

## Contributing
Contributions are welcome. Please fork the repository and submit pull requests for improvements or bug fixes.

