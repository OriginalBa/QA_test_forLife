# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # 1. Запуск браузера Chrome
# driver = webdriver.Chrome()
#
# try:
#     # 2. Открытие страницы
#     driver.get("https://qa-guru.github.io/one-page-form/login.html")
#     driver.maximize_window()
#     # driver.implicitly_wait(3)
#     time.sleep(3)  # Пауза, чтобы визуально заметить открытие
#
#     # 3. Поиск элементов и заполнение полей
#     # Находим поле login-input по его ID и вводим текст #login-input
#     login_input_field = driver.find_element(By.ID, "login-input")
#
#     login_data = "user1"
#     login_input_field.send_keys(login_data)
#     # Находим поле #password-input по его ID и вводим текст
#     password_input_field = driver.find_element(By.ID, "password-input")
#     password_input_field.send_keys("password1")
#
#     # Находим кнопку Login по ее ID и кликаем #submit-button
#     login_button = driver.find_element(By.ID, "submit-button")
#     login_button.click()
#
#     # 4. Проверка результата
#     time.sleep(3)  # Пауза, чтобы увидеть результат отправки
#
#     # Находим блок с отправленными данными #welcome-message #success-panel
#     result_message = driver.find_element(By.ID, "welcome-message")
#
#     # Проверяем, что в блоке результата появился успешный текст входа
#     assert f"Welcome, {login_data}!" in result_message.text
#     #print(login_input_field.text)
#     #print(result_message.text)
#     print("Тест успешно пройден!")
#
# finally:
#     # 5. Закрытие браузера в любом случае
#     driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestModelFormLogin:

    login_input_locator = (By.ID, "login-input")
    password_input_locator = (By.ID, "password-input")
    submit_button_locator = (By.ID, "submit-button")
    logout_button_locator = (By.ID, "logout-button")
    welcome_message_locator = (By.ID, "welcome-message")
    error_locator = (By.ID, "error-message")


    def __init__(self, url):
        self.driver = None
        self.url = url


    def test_set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)  # Пауза, чтобы визуально заметить открытие

    def test_tear_down(self):
        # 5. Закрытие браузера в любом случае
        self.driver.quit()

    def login_field(self, login):
        self.driver.find_element(*self.login_input_locator).send_keys(login)

    def password_field(self, password):
        self.driver.find_element(*self.password_input_locator).send_keys(password)

    def submit_button(self):
        self.driver.find_element(*self.submit_button_locator).click()

    def logout_button(self):
        self.driver.find_element(*self.logout_button_locator).click()

    def welcome_message_text(self):
       return self.driver.find_element(*self.welcome_message_locator).text

    def error_text(self):
       return self.driver.find_element(*self.error_locator).text

def test_01_positive():
    login_form = TestModelFormLogin(url = "https://qa-guru.github.io/one-page-form/login.html")
    login_form.test_set_up()
    login_form.login_field("user1")
    login_form.password_field("password1")
    login_form.submit_button()
    assert login_form.welcome_message_text() == "Welcome, user1!"
    login_form.logout_button()
    login_form.test_tear_down()

def test_02_negative():
    login_form = TestModelFormLogin(url = "https://qa-guru.github.io/one-page-form/login.html")
    login_form.test_set_up()
    login_form.submit_button()
    assert login_form.error_text() == "Login and password are required (minimum 3 and 6 characters)"
    login_form.test_tear_down()

def test_03_negative():
    login_form = TestModelFormLogin(url = "https://qa-guru.github.io/one-page-form/login.html")
    login_form.test_set_up()
    login_form.login_field("user5")
    login_form.password_field("password1")
    login_form.submit_button()
    assert login_form.error_text() == "Wrong login or password"
    login_form.test_tear_down()

def test_04_negative():
    login_form = TestModelFormLogin(url = "https://qa-guru.github.io/one-page-form/login.html")
    login_form.test_set_up()
    login_form.login_field("user1")
    login_form.password_field("password5")
    login_form.submit_button()
    assert login_form.error_text() == "Wrong login or password"
    login_form.test_tear_down()