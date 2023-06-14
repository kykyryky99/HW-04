from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets1(open_browser_and_login):
    pytest.driver.find_element(By.XPATH, '//*[text()="Мои питомцы"]').click()

    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))

    elem_with_count_pets = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
    elem_with_count_pets_text: str = elem_with_count_pets.text
    pets_blocks_text = elem_with_count_pets_text.split('\n')

    assert len(pets_blocks_text) == 4, 'Count text block not equal 4'

    count_pets_block_text = pets_blocks_text[1]

    assert len(count_pets_block_text) != 0, 'Length string count pets is empty'

    count_pets_text = count_pets_block_text.split(' ')

    assert len(count_pets_text) == 2, 'String with count pets is invalid'

    count_pets = int(count_pets_text[-1])

    elem_table_tbody = pytest.driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')
    elem_table_all_tr = elem_table_tbody.find_elements(By.TAG_NAME, "tr")

    assert count_pets == len(elem_table_all_tr), 'Count pets not equal count rows in table'




def test_show_my_pets_with_foto(open_browser_and_login):
    # goal: Проверить что хотябы у половины питомцев есть фото.
    # task_1: Из таблички достать все th
    # task_3: Проверить все th на наличие не пустого src
    # task_2: Посчитать сколько tr в таблице
    # task_4: Сравнить половину tr c количеством th
    pytest.driver.find_element(By.XPATH, '//*[text()="Мои питомцы"]').click()

    pytest.driver.implicitly_wait(5)
    # task_1
    elem_table_tbody = pytest.driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')
    elem_table_all_th: list = elem_table_tbody.find_elements(By.TAG_NAME, "th")

    # task_2
    elem_table_rows = elem_table_tbody.find_elements(By.TAG_NAME, "tr")
    if len(elem_table_rows) == 0:
        return

    # task_3
    elem_table_valid_th = []
    for elem_th in elem_table_all_th:
        elem_img: WebElement = elem_th.find_element(By.TAG_NAME, "img")
        if elem_img.get_attribute('src') != '' and elem_img.get_attribute('src') is not None:
            elem_table_valid_th.append(elem_th)

    # task_4
    elem_table_polovina_rows = int(len(elem_table_rows) * 0.5)

    assert elem_table_polovina_rows <= len(elem_table_valid_th), 'Count photos less than 0.5 * count rows from table'

def test_my_pets_have_name_age_breed(open_browser_and_login):
    # goal: У всех питомцев есть имя, возраст и порода.
    # task_1: Из таблички достать все td
    # task_2: Проверить все td на наличие текста
    # task_3: если в какойто td пусто вернуть "Питомец имеет пустое поле"

    pytest.driver.find_element(By.XPATH, '//*[text()="Мои питомцы"]').click()
    # task_1
    elem_table_tbody = pytest.driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')
    elem_table_all_td = elem_table_tbody.find_elements(By.TAG_NAME, "td")

    # task_2:
    elem_table_empty = []
    for elem_td in elem_table_all_td:
        if elem_td == '':
            elem_table_empty.append(elem_td)

    # task_3
    assert len(elem_table_empty) >= 1, 'The pet has an empty field'


def test_my_pet_have_diferent_name(open_browser_and_login):
    # goal: У всех питомцев разные имена.
    # task_1: Из таблички достать все tr и из tr взять первый td
    # task_2: Как отделить имена от породы и возраста??
    # task_3: из всех имен найти одинаковые имена
    pytest.driver.find_element(By.XPATH, '//*[text()="Мои питомцы"]').click()

    # task_1
    elem_table_tbody = pytest.driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')
    elem_table_all_td1 = elem_table_tbody.find_elements(By.XPATH, "//td[1]")

    name_set = set(elem_table_all_td1????)
   assert elem_table_all_td1 = name_set:???

    assert 1 < 3




