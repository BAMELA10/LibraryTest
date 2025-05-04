from LibraryTest.core.exception_test_page import ExceptionTestPage

#Test case 3 InvalidElementStateException
exception_page = ExceptionTestPage("https://practicetestautomation.com/", "practice-test-exceptions/", "test")
exception_page.check_InvalidElementStateException(
    confirmation_message='Row 2 was added',
    id_edit_button='edit_btn',
    xpath_input_row1='//*[@id="row1"]/input',
    xpath_save_button='//*[@id="save_btn"]'
)
