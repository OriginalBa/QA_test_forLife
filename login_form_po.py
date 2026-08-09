from seleniumpagefactory.Pagefactory import PageFactory


class LoginFormPO(PageFactory):
    locators = {
        "login_field": ("ID", "login-input"),
        "password_field": ("ID", "password-input"),
        "submit_button": ("ID", "submit-button"),
        "logout_button": ("ID", "logout-button"),
        "welcome_message": ("ID", "welcome-message"),
        "error_message": ("ID", "error-message"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-guru.github.io/one-page-form/login.html"
        self.timeout = 10

    def open(self):
        self.driver.get(self.url)

    def set_login_field(self, login):
        self.login_field.set_text(login)

    def set_password_field(self, password):
        self.password_field.set_text(password)

    def click_submit_button(self):
        self.submit_button.click_button()

    def click_logout_button(self):
        self.logout_button.click_button()

    def get_welcome_message_text(self):
        return self.welcome_message.get_text()

    def get_error_text(self):
        return self.error_message.get_text()
