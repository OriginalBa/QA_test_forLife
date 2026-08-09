import allure
import pytest
from login_form_po import LoginFormPO


@allure.epic("UI Automation")
@allure.feature("Login Form")
@allure.story("Успешная отправка формы")
@allure.title("Успешная авторизация с валидными данными")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_successful_login(driver):
    login_form = LoginFormPO(driver)
    login_form.open()
    login_form.set_login_field("user1")
    login_form.set_password_field("password1")
    login_form.click_submit_button()
    assert login_form.get_welcome_message_text() == "Welcome, user1!"
    login_form.click_logout_button()


@allure.epic("UI Automation")
@allure.feature("Login Form")
@allure.story("Отклонение отправки формы")
@allure.title("Авторизация с некорректными данными: {login}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.parametrize("login, password, expected_error",
                         [
                             ("юзер1", "пароль1", "Wrong login or password"),  # Кириллица
                             ("A", "B", "Login must be at least 3 characters"),  # Слишком короткие (менее 3 симв.)
                             ("Addr 1/2", "Addr 3 & 4", "Wrong login or password"),  # Спецсимволы
                             ("user 1", "password 1", "Wrong login or password"),  # Пробелы
                         ],
                         )
def test_failed_login(driver, login, password, expected_error):
    login_form = LoginFormPO(driver)
    login_form.open()
    login_form.set_login_field(login)
    login_form.set_password_field(password)
    login_form.click_submit_button()
    assert login_form.get_error_text() == expected_error
