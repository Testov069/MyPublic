mport pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
import time


@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest_driver.get('http://petfriends.skillfactory.ru/login')

    yield pytest_driver

    pytest_driver.quit()


def test_show_my_pets(testing):
    pytest_driver = testing
    # Вводим email
    pytest_driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    pytest_driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest_driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(3)



    images = pytest_driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest_driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest_driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
