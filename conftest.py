import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def open_browser_and_login():
    service = Service(executable_path=r"C:\Users\Volk\Desktop\chromedriver.exe")
    pytest.driver = webdriver.Chrome(service=service)
    # Переходим на страницу авторизации
    pytest.driver.get("https://petfriends.skillfactory.ru/login")

    pytest.driver.find_element(By.ID, 'email').send_keys('Volkov@gmail.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('020700')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    yield

    pytest.driver.quit()
