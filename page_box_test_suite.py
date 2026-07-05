from page_box_po import PageBoxPO
from selenium import webdriver


class PageBoxSuite:

    def __init__(self):
        self.driver = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def test_positive_two_fields(self):
        print("test_positive_two_fields: start")
        self.set_up()
        page_form = PageBoxPO(self.driver)
        try:
            page_form.input_full_name("Роман Халимов")
            page_form.input_email("ian@neexample.com")
            page_form.click_submit()
            result_text = page_form.result()
            assert "Роман Халимов" in result_text
            assert "ian@neexample.com" in result_text
            print("Тест успешно пройден!")
        finally:
            self.tear_down()
        print("test_positive_two_fields: end")

    def test_positive_all_fields(self):
        print("test_positive_all_fields: start")
        self.set_up()
        page_form = PageBoxPO(self.driver)

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
            self.tear_down()
        print("test_positive_all_fields: end")

    def test_negative_mail(self):
        print("test_negative_mail: start")
        self.set_up()
        page_form = PageBoxPO(self.driver)

        try:
            page_form.input_full_name("Роман Халимов")
            page_form.input_email("ian@ne_example.com")
            page_form.click_submit()
            error_message = page_form.get_email_validation_message()
            assert 'Часть адреса после символа "@" не должна содержать символ "_"' in error_message
            print("Негативный тест успешно пройден!")
        finally:
            self.tear_down()
        print("test_negative_mail: end")

    def test_negative_nosimbol(self):
        print("test_negative_nosimbol: start")
        self.set_up()
        page_form = PageBoxPO(self.driver)

        try:
            page_form.input_full_name("Роман Халимов")
            page_form.input_email("ianne_example.com")
            page_form.click_submit()
            error_message = page_form.get_email_validation_message()
            assert 'Адрес электронной почты должен содержать символ "@". В адресе "ianne_example.com" отсутствует символ "@".' in error_message
            print("Негативный тест успешно пройден!")
        finally:
            self.tear_down()
        print("test_negative_nosimbol: end")

    def test_sql_injection(self):
        print("test_sql_injection: start")
        self.set_up()
        page_form = PageBoxPO(self.driver)

        try:
            page_form.input_full_name("Роман Халимов")
            page_form.input_email("SELECT SUBSTRING(password,1,1")
            page_form.click_submit()
            error_message = page_form.get_email_validation_message()
            assert 'Адрес электронной почты должен содержать символ "@". В адресе "SELECT SUBSTRING(password,1,1" отсутствует символ "@".' in error_message
            print("Негативный тест успешно пройден!")
        finally:
            self.tear_down()
        print("test_sql_injection: end")


test_suite = PageBoxSuite()
test_suite.test_positive_two_fields()
test_suite.test_positive_all_fields()
test_suite.test_negative_mail()
test_suite.test_negative_nosimbol()
test_suite.test_sql_injection()
