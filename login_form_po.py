from selenium.webdriver.common.by import By


class LoginFormPO:
    login_input_locator = (By.ID, "login-input")
    password_input_locator = (By.ID, "password-input")
    submit_button_locator = (By.ID, "submit-button")
    logout_button_locator = (By.ID, "logout-button")
    welcome_message_locator = (By.ID, "welcome-message")
    error_locator = (By.ID, "error-message")

    def __init__(self, driver):
        self.driver = driver

    # Low Level action
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

# В одном файле находится один класс. Отдельно взятые функции в проекте не используются
# шаг 1 - класс разбить на два класса. Сделать еще один класс loginTestSuite - в него пойдут тесты
# шаг 2 добавить логгироание в тесты
# щаг 3 перенести сетап м тирдаун
