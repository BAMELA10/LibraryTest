from Test_framework_lib.login_test_page import LoginTestPage
#Test case 3 Negative password test
login_page = LoginTestPage("","","")
login_page.negative_password_test()