import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def session_lifecycle():
    print("\n\n>>> [SESSION SETUP] Подключение к БД / Запуск сервера <<<")
    yield
    print("\n>>> [SESSION TEARDOWN] Отключение от БД / Остановка сервера <<<")


@pytest.fixture(scope="function", autouse=True)
def driver():
    print("\n\n>>> Открываем браузер <<<")
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    print("\n\n>>> Закрываем браузер <<<")
    driver.quit()
