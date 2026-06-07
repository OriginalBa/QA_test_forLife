import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestModelForm1:

    full_name_locator = "userName"
    email_locator = "userEmail"
    submit_locator = "submit"
    current_locator = "currentAddress"
    permanent_locator = "permanentAddress"
    result_locator = "output"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_set_up(self):
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        time.sleep(3)  # Пауза, чтобы визуально заметить открытие

    def test_tear_down(self):
        # 5. Закрытие браузера в любом случае
        self.driver.quit()



    def test_1(self):

        try:
            # 2. Открытие страницы
            self.test_set_up()

            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Роман Халимов")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(By.ID, self.email_locator)
            email_field.send_keys("ian@neexample.com")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(By.ID, self.submit_locator)
            submit_button.click()

            # 4. Проверка результата
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(By.ID, self.result_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Роман Халимов" in result_box.text
            print("Тест успешно пройден!")

        finally:
            # 5. Закрытие браузера в любом случае
            self.test_tear_down()

    def test_2(self):

        try:
            # 2. Открытие страницы
            self.test_set_up()

            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Роман Халимов")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(By.ID, self.email_locator)
            email_field.send_keys("ian@neexample.com")

            # Находим поле Current Address и заполняем его
            current_address = self.driver.find_element(By.ID, self.current_locator) #currentAddress
            current_address.send_keys("Москва, Севильский бульвар 1, кв 76")

            # Находим поле Permanent Address и также заполняем его
            permanent_address = self.driver.find_element(By.ID, self.permanent_locator) #permanentAddress
            permanent_address.send_keys("Москва, Несевильский небульвар 1, кв. 76")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(By.ID, self.submit_locator)
            submit_button.click()

            # 4. Проверка результата
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(By.ID, self.result_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Роман Халимов" in result_box.text
            assert "Москва, Севильский бульвар 1, кв 76" in result_box.text
            print("Тест успешно пройден!")

        finally:
            # 5. Закрытие браузера в любом случае
            self.test_tear_down()

    def test_3(self):

        try:
            # 2. Открытие страницы
            self.test_set_up()

            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Роман Халимов")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(By.ID, self.email_locator)
            email_field.send_keys("ian@ne_example.com")

            # Находим поле Current Address и заполняем его
            current_address = self.driver.find_element(By.ID, self.current_locator)  # currentAddress
            current_address.send_keys("Москва, Севильский бульвар 1, кв 76")

            # Находим поле Permanent Address и также заполняем его
            permanent_address = self.driver.find_element(By.ID, self.permanent_locator)  # permanentAddress
            permanent_address.send_keys("Москва, Несевильский небульвар 1, кв. 76")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(By.ID, self.submit_locator)
            submit_button.click()

            # 4. Проверка результата
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(By.ID, self.result_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Роман Халимов" is not result_box.text
            assert "Москва, Севильский бульвар 1, кв 76" is not result_box.text
            print("Тест не пройден!")

        finally:
            # 5. Закрытие браузера в любом случае
            self.test_tear_down()

    def test_4(self):

        try:
            # 2. Открытие страницы
            self.test_set_up()

            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Роман Халимов")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(By.ID, self.email_locator)
            email_field.send_keys("ianne_example.com")

            # Находим поле Current Address и заполняем его
            current_address = self.driver.find_element(By.ID, self.current_locator)  # currentAddress
            current_address.send_keys("Москва, Севильский бульвар 1, кв 76")

            # Находим поле Permanent Address и также заполняем его
            permanent_address = self.driver.find_element(By.ID, self.permanent_locator)  # permanentAddress
            permanent_address.send_keys("Москва, Несевильский небульвар 1, кв. 76")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(By.ID, self.submit_locator)
            submit_button.click()

            # 4. Проверка результата
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(By.ID, self.result_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Роман Халимов" is not result_box.text
            assert "Москва, Севильский бульвар 1, кв 76" is not result_box.text
            assert "ian@neexample.com" is not result_box.text
            print("Тест не пройден!")

        finally:
            # 5. Закрытие браузера в любом случае
            self.test_tear_down()

    def test_5(self):

        try:
            # 2. Открытие страницы
            self.test_set_up()

            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Иван Иванов")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(By.ID, self.email_locator)
            email_field.send_keys("AND (SELECT SUBSTRING(password,1,1) FROM users WHERE id=1) = 'a'")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(By.ID, self.submit_locator)
            submit_button.click()

            # 4. Проверка результата
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(By.ID, self.result_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Иван Иванов" is not result_box.text
            print("Тест не пройден!")

        finally:
            # 5. Закрытие браузера в любом случае
            self.test_tear_down()

test_object1 = TestModelForm1()
test_object1.test_1()
test_object2 = TestModelForm1()
test_object2.test_2()
test_object3 = TestModelForm1()
test_object3.test_3()
test_object4 = TestModelForm1()
test_object4.test_4()
test_object5 = TestModelForm1()
test_object5.test_5()

