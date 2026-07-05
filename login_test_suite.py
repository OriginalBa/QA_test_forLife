from login_form_po import LoginFormPO
from selenium import webdriver


class LoginTestSuite:

    def __init__(self):
        self.driver = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def test_fill_all_fields(self):
        print("test_fill_all_fields: start")
        self.set_up()
        login_form = LoginFormPO(self.driver)
        try:
            login_form.set_login_field("user1")
            login_form.set_password_field("password1")
            login_form.click_submit_button()
            assert login_form.get_welcome_message_text() == "Welcome, user1!"
            login_form.click_logout_button()
        finally:
            self.tear_down()
        print("test_fill_all_fields: end")

    def test_02_negative_nologin(self):
        print("test_02_negative_nologin: start")
        self.set_up()
        login_form = LoginFormPO(self.driver)
        try:
            login_form.click_submit_button()
            assert login_form.get_error_text() == "Login and password are required (minimum 3 and 6 characters)"
        finally:
            self.tear_down()
        print("test_02_negative_nologin: end")

    def test_03_negative_wronglogin(self):
        print("test_03_negative_wronglogin: start")
        self.set_up()
        login_form = LoginFormPO(self.driver)

        try:
            login_form.set_login_field("user5")
            login_form.set_password_field("password1")
            login_form.click_submit_button()
            assert login_form.get_error_text() == "Wrong login or password"
        finally:
            self.tear_down()
        print("test_03_negative_wronglogin: end")

    def test_04_negative_wrongpassword(self):
        print("test_04_negative_wrongpassword: start")
        self.set_up()
        login_form = LoginFormPO(self.driver)

        try:
            login_form.set_login_field("user1")
            login_form.set_password_field("password5")
            login_form.click_submit_button()
            assert login_form.get_error_text() == "Wrong login or password"
        finally:
            self.tear_down()
        print("test_04_negative_wrongpassword: end")


test_suite = LoginTestSuite()
test_suite.test_fill_all_fields()
test_suite.test_02_negative_nologin()
test_suite.test_03_negative_wronglogin()
test_suite.test_04_negative_wrongpassword()
