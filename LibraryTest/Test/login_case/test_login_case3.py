from LibraryTest.core.login_test_page import LoginTestPage

#Test case 3 Negative password test
login_page = LoginTestPage("https://practicetestautomation.com/","practice-test-login/")
login_page.invalid_credentials_test(
    username="student",
    password="incorrectPassword",
    xpath_username="//input[@id='username']",
    xpath_password="//input[@id='password']",
    xpath_login_button='//*[@id="submit"]',
    xpath_error_message_box='//*[@id="error"]',
    error_message="Your username is invalid!"
)