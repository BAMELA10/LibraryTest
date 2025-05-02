from LibraryTest.Test_framework_lib.login_test_page import LoginTestPage

#Test case 2 Negative username test
login_page = LoginTestPage("https://practicetestautomation.com/","practice-test-login/")
login_page.invalid_credentials_test(
    username="incorrectUser",
    password="Password123",
    xpath_username="//input[@id='username']",
    xpath_password="//input[@id='password']",
    xpath_login_button='//*[@id="submit"]',
    xpath_error_message_box='//*[@id="error"]',
    error_message="Your username is invalid!"
)