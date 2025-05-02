from LibraryTest.Test_framework_lib.login_test_page import LoginTestPage

#Test case 1 positive login test
login_page = LoginTestPage("https://practicetestautomation.com/","practice-test-login/")
login_page.postive_login_test(
    username="student",
    password="Password123",
    xpath_username="//input[@id='username']",
    xpath_password="//input[@id='password']",
    xpath_login_button='//*[@id="submit"]',
    xpath_logout_button="/html/body/div/div/section/div/div/article/div[2]/div/div/div/a",
    login_url="https://practicetestautomation.com/logged-in-successfully/",
    confirmation_message="Congratulations"
)