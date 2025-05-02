from Test_framework_lib.exception_test_page import ExceptionTestPage

#Test case 1 NoSuchElementException
exception_page = ExceptionTestPage("","")
exception_page.check_NoSuchElementException()
