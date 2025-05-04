from LibraryTest.core.exception_test_page import ExceptionTestPage

#Test case 4 StaleElementReferenceException
exception_page = ExceptionTestPage("https://practicetestautomation.com/", "practice-test-exceptions/")
exception_page.check_StaleElementReferenceException(
    id_instruction='instructions',
    xpath_add_button='//*[@id="add_btn"]'
)
