from LibraryTest.core.exception_test_page import ExceptionTestPage

#Test case 2 ElementNotInteractableException
exception_page = ExceptionTestPage("https://practicetestautomation.com/", "practice-test-exceptions/", "test")
exception_page.check_ElementNotInteractableException(
     xpath_add_button='//*[@id="add_btn"]',
    xpath_row2='//*[@id="row2"]',
    xpath_input_row2='//*[@id="row2"]/input',
    id_confirmation='confirmation',
    name_save_button='Save'
)
