from page_box_po import PageBoxPO
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.epic("UI Automation")
@allure.feature("Text Box Form")
@allure.story("Успешная отправка формы")
@allure.title("Отправка формы с корректными данными")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize("name, email, current_address, permanent_address", [
    ("John Doe", "john@example.com", "123 Elm St", "456 Oak St"),  # Стандартный кейс
    ("Иван Иванов", "ivan@mail.ru", "ул. Ленина, д. 1", "ул. Пушкина, д. 2"),  # Кириллица
    ("A", "a@b.cc", "B", "C"),  # Минимальная длина строк
    ("Name-With Dash", "dash@email.co.uk", "Addr 1/2", "Addr 3 & 4"),  # Спецсимволы в полях
    ("   Рома   ", "ian@neexample.com", "  Москва, Севильский бульвар 1, кв 76  ",
     "  Москва, Несевильский небульвар 1, кв. 76  "),  # Строки с пробелами
])
def test_positive_all_fields(driver, name, email, current_address, permanent_address):
    print("test_positive_all_fields: start")
    page_form = PageBoxPO(driver)
    page_form.open()
    page_form.fill_form(name, email, current_address, permanent_address)
    page_form.click_submit_button()
    output = page_form.get_result_data()
    assert output is not None, "Блок с результатами не отобразился"
    assert output["name"] == name.strip()
    assert output["email"] == email.strip()
    assert output["current_address"] == current_address.strip()
    assert output["permanent_address"] == permanent_address.strip()
    print("test_positive_all_fields: end")


@allure.feature("Проверка на корректность заполнения")
@allure.story("Некорректное поле email")
@allure.title("Отправка формы с заполненными не всеми полями")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize("invalid_email", [
    "plainaddress",  # Нет собаки и домена
    "@no-local-part.com",  # Нет имени пользователя
    pytest.param("john.doe@com", marks=pytest.mark.xfail(reason="Ожидаемая ошибка: нет доменной зоны верхнего уровня")),
    pytest.param("john@missing-dot", marks=pytest.mark.xfail(reason="Ожидаемая ошибка: нет точки в домене")),
    "ian@@example.com",  # Две собаки
    "ian@example..com",  # Две точки подряд
])
def test_invalid_email(driver, invalid_email):
    print("test_invalid_email: start")
    page_form = PageBoxPO(driver)
    page_form.open()
    page_form.fill_form("Test", invalid_email)
    page_form.click_submit_button()
    output = page_form.get_result_data()
    assert output is None or page_form.is_email_error_present(), f"Email '{invalid_email}' не должен быть принят системой"
    print("test_invalid_email: end")


@allure.feature("Безопасность")
@allure.story("Защита от XSS и HTML-инъекций")
@allure.title("Обработка потенциально опасного ввода")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regress
@pytest.mark.parametrize("security_payload", [
    "<script>alert('xss')</script>",  # Базовый XSS скрипт
    "1' OR '1'='1",  # Базовая SQL-инъекция
    ":):):):))))::;)",  # Суррогатные пары (Эмодзи)
    "<div>HTML injection</div>"  # Теги верстки
])
def test_sql_injection(driver, security_payload):
    print("test_sql_injection: start")
    page_form = PageBoxPO(driver)
    page_form.open()
    page_form.fill_form(name=security_payload, current_address=security_payload, permanent_address=security_payload)
    page_form.click_submit_button()
    output = page_form.get_result_data()
    raw_element = driver.find_element(By.ID, "name")
    output_html = raw_element.get_attribute("innerHTML")
    if "<script>" in security_payload:
        with pytest.raises(AssertionError, match="УЯЗВИМОСТЬ XSS!"):
            assert "<script>" not in output_html.lower(), "УЯЗВИМОСТЬ XSS! Скрипт внедрился в DOM как активный тег!"
    elif "<div>" in security_payload:
        assert "<div>" not in output_html.lower(), "УЯЗВИМОСТЬ HTML-инъекции! Тег отрендерился на странице!"
    else:
        assert output is not None, "Форма упала при вводе спецсимволов"
        assert output["name"] == security_payload
        assert output["current_address"] == security_payload
        assert output["permanent_address"] == security_payload
    print("test_sql_injection: end")
