from selenium import webdriver
from selenium.webdriver.common.by import By


class TestModelFormLogin:
    login_input_locator = (By.ID, "login-input")
    password_input_locator = (By.ID, "password-input")
    submit_button_locator = (By.ID, "submit-button")
    logout_button_locator = (By.ID, "logout-button")
    welcome_message_locator = (By.ID, "welcome-message")
    error_locator = (By.ID, "error-message")

    def __init__(self):
        self.wait = None
        self.driver = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def set_login_field(self, login):
        self.driver.find_element(*self.login_input_locator).send_keys(login)

    def set_password_field(self, password):
        self.driver.find_element(*self.password_input_locator).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button_locator).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button_locator).click()

    def get_welcome_message_text(self):
        return self.driver.find_element(*self.welcome_message_locator).text

    def get_error_text(self):
        return self.driver.find_element(*self.error_locator).text


def test_fill_all_fields():
    login_form = TestModelFormLogin()
    login_form.set_up()
    try:
        login_form.set_login_field("user1")
        login_form.set_password_field("password1")
        login_form.click_submit_button()
        assert login_form.get_welcome_message_text() == "Welcome, user1!"
        login_form.click_logout_button()
    finally:
        login_form.tear_down()


def test_02_negative_nologin():
    login_form = TestModelFormLogin()
    login_form.set_up()
    try:
        login_form.click_submit_button()
        assert login_form.get_error_text() == "Login and password are required (minimum 3 and 6 characters)"
    finally:
        login_form.tear_down()


def test_03_negative_wronglogin():
    login_form = TestModelFormLogin()
    login_form.set_up()
    try:
        login_form.set_login_field("user5")
        login_form.set_password_field("password1")
        login_form.click_submit_button()
        assert login_form.get_error_text() == "Wrong login or password"
    finally:
        login_form.tear_down()


def test_04_negative_wrongpassword():
    login_form = TestModelFormLogin()
    login_form.set_up()
    try:
        login_form.set_login_field("user1")
        login_form.set_password_field("password5")
        login_form.click_submit_button()
        assert login_form.get_error_text() == "Wrong login or password"
    finally:
        login_form.tear_down()
