from Test_framework_lib.login_test_page import LoginTestPage
#Test case 2 Negative username test
login_page = LoginTestPage("","","")
login_page.negative_username_test()