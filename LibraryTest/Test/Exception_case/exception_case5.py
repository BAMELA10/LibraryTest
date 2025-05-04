from LibraryTest.core.exception_test_page import ExceptionTestPage

#Test case 5 TimeoutException
exception_page = ExceptionTestPage("https://practicetestautomation.com/", "practice-test-exceptions/")
exception_page.check_TimeoutException(
    xpath_add_button='//*[@id="add_btn"]',
    xpath_input_row2='//*[@id="row2"]/input',
)
