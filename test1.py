import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Запуск браузера Chrome
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Иванов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivan@example.com")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Иван Иванов" in result_box.text
    print("Тест успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()

#Тест 2 Current Address + Permanent Address + assert на адрес
 # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Роман Халимов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ian@neexample.com")

    # Находим поле Current Address и заполняем его
    current_address = driver.find_element(By.ID, "currentAddress") #currentAddress
    current_address.send_keys("Москва, Севильский бульвар 1, кв 76")

    # Находим поле Permanent Address и также заполняем его
    permanent_address = driver.find_element(By.ID, "permanentAddress") #permanentAddress
    permanent_address.send_keys("Москва, Несевильский небульвар 1, кв. 76")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Роман Халимов" in result_box.text
    assert "Москва, Севильский бульвар 1, кв 76" in result_box.text
    print("Тест успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()


# Тест 3 негатив с "_" в почтовом адресе
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Роман Халимов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ian@ne_example.com")

    # Находим поле Current Address и заполняем его
    current_address = driver.find_element(By.ID, "currentAddress")  # currentAddress
    current_address.send_keys("Москва, Севильский бульвар 1, кв 76")

    # Находим поле Permanent Address и также заполняем его
    permanent_address = driver.find_element(By.ID, "permanentAddress")  # permanentAddress
    permanent_address.send_keys("Москва, Несевильский небульвар 1, кв. 76")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    # assert "Роман Халимов" in result_box.text
    # assert "Москва, Севильский бульвар 1, кв 76" in result_box.text
    print("Тест не пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()


# Тест 4 негатив без @ в почтовом адресе
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Роман Халимов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ianne_example.com")

    # Находим поле Current Address и заполняем его
    current_address = driver.find_element(By.ID, "currentAddress")  # currentAddress
    current_address.send_keys("Москва, Севильский бульвар 1, кв 76")

    # Находим поле Permanent Address и также заполняем его
    permanent_address = driver.find_element(By.ID, "permanentAddress")  # permanentAddress
    permanent_address.send_keys("Москва, Несевильский небульвар 1, кв. 76")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    # assert "Роман Халимов" in result_box.text
    # assert "Москва, Севильский бульвар 1, кв 76" in result_box.text
    # assert "ian@neexample.com" in result_box.text
    print("Тест не пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()

# Тест 5 с инъекцией в бд через поле mail
# 1. Запуск браузера Chrome
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Иванов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("AND (SELECT SUBSTRING(password,1,1) FROM users WHERE id=1) = 'a'")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    # assert "Иван Иванов" in result_box.text
    print("Тест не пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()