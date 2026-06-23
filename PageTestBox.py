from selenium import webdriver
from selenium.webdriver.common.by import By


class TestModelForm1:
    full_name_locator = (By.ID, "userName")
    email_locator = (By.ID, "userEmail")
    submit_locator = (By.ID, "submit")
    current_locator = (By.ID, "currentAddress")
    permanent_locator = (By.ID, "permanentAddress")
    result_locator = (By.ID, "output")
    email_css_locator = (By.CSS_SELECTOR, "input[type='email']")

    def __init__(self):
        self.driver = None
        self.wait = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def input_full_name(self, name):
        self.driver.find_element(*self.full_name_locator).send_keys(name)

    def input_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def input_current_address(self, address):
        self.driver.find_element(*self.current_locator).send_keys(address)

    def input_permanent_address(self, p_address):
        self.driver.find_element(*self.permanent_locator).send_keys(p_address)

    def click_submit(self):
        submit_btn = self.driver.find_element(*self.submit_locator)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        submit_btn.click()

    def result(self):
        return self.driver.find_element(*self.result_locator).text

    def get_email_validation_message(self):
        email_field = self.driver.find_element(*self.email_css_locator)
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", email_field)
        return validation_message


def test_positive_two_fields():
    page_form = TestModelForm1()
    page_form.set_up()
    try:
        page_form.input_full_name("Роман Халимов")
        page_form.input_email("ian@neexample.com")
        page_form.click_submit()
        result_text = page_form.result()
        assert "Роман Халимов" in result_text
        assert "ian@neexample.com" in result_text
        print("Тест успешно пройден!")
    finally:
        page_form.tear_down()


def test_positive_all_fields():
    page_form = TestModelForm1()
    page_form.set_up()
    try:
        page_form.input_full_name("Роман Халимов")
        page_form.input_email("ian@neexample.com")
        page_form.input_current_address("Москва, Севильский бульвар 1, кв 76")
        page_form.input_permanent_address("Москва, Несевильский небульвар 1, кв. 76")
        page_form.click_submit()
        result_text = page_form.result()
        assert "Роман Халимов" in result_text
        assert "ian@neexample.com" in result_text
        assert "Москва, Севильский бульвар 1, кв 76" in result_text
        assert "Москва, Несевильский небульвар 1, кв. 76" in result_text
        print("Тест успешно пройден!")
    finally:
        page_form.tear_down()


def test_negative_mail():
    page_form = TestModelForm1()
    page_form.set_up()
    try:
        page_form.input_full_name("Роман Халимов")
        page_form.input_email("ian@ne_example.com")
        page_form.click_submit()
        error_message = page_form.get_email_validation_message()
        assert 'Часть адреса после символа "@" не должна содержать символ "_"' in error_message
        print("Негативный тест успешно пройден!")
    finally:
        page_form.tear_down()


def test_negative_nosimbol():
    page_form = TestModelForm1()
    page_form.set_up()
    try:
        page_form.input_full_name("Роман Халимов")
        page_form.input_email("ianne_example.com")
        page_form.click_submit()
        error_message = page_form.get_email_validation_message()
        assert 'Адрес электронной почты должен содержать символ "@". В адресе "ianne_example.com" отсутствует символ "@".' in error_message
        print("Негативный тест успешно пройден!")
    finally:
        page_form.tear_down()


def test_sql_injection():
    page_form = TestModelForm1()
    page_form.set_up()
    try:
        page_form.input_full_name("Роман Халимов")
        page_form.input_email("SELECT SUBSTRING(password,1,1")
        page_form.click_submit()
        error_message = page_form.get_email_validation_message()
        assert 'Адрес электронной почты должен содержать символ "@". В адресе "SELECT SUBSTRING(password,1,1" отсутствует символ "@".' in error_message
        print("Негативный тест успешно пройден!")
    finally:
        page_form.tear_down()
