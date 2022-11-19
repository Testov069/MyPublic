import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from settings import *




@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest_driver.get('https://b2c.passport.rt.ru/')

    yield pytest_driver

    pytest_driver.quit()

#1 Позитивный тест-кейс: авторизация по кнопке "телефон" с корректными данными

def test_homepage_1(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_phone)
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text == 'Тестов Тест'
    time.sleep(3)

#2 Позитивный тест-кейс: авторизация по кнопке "почта" с корректными данными

def test_homepage_2(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text == 'Тестов Тест'
    time.sleep(3)

#3 Позитивный тест-кейс: авторизация по кнопке "логин" с корректными данными

def test_homepage_3(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_login)
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text == 'Тестов Тест'
    time.sleep(3)

#4 Позитивный тест-кейс: авторизация по кнопке "лицевой счет" с корректными данными

def test_homepage_4(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_ls)
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text == 'Тестов Тест'
    time.sleep(3)


#5 Негативный тест-кейс: авторизация по кнопке "почта" некорректным полем "почта"

def test_homepage_5(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('test@test')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'
    time.sleep(3)

#6 Негативный тест-кейс: авторизация по кнопке "почта" некорректным полем "пароль"

def test_homepage_6(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest_driver.find_element(By.ID, 'password').send_keys('password')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'
    time.sleep(3)

#7 Негативный тест-кейс: авторизация по кнопке "почта" c пустым полем "почта"

def test_homepage_7(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'

#8 Негативный тест-кейс: авторизация по кнопке "почта" c пустым полем "пароль"

def test_homepage_8(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest_driver.find_element(By.ID, 'password').send_keys('')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'

#9 Негативный тест-кейс: авторизация по кнопке "телефон" c некорректным полем "телефон"

def test_homepage_9(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('91111111111')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'

#10 Негативный тест-кейс: авторизация ппо кнопке "телефон" c некорректным  полем "пароль"

def test_homepage_10(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_phone)
    pytest_driver.find_element(By.ID, 'password').send_keys('password')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'


#11 Негативный тест-кейс: авторизация по кнопке "телефон" c пустым полем "телефон"

def test_homepage_11(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text != 'Тестов Тест'


#12 Негативный тест-кейс: авторизация по кнопке "телефон" c пустым полем "пароль"

def test_homepage_12(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_phone)
    pytest_driver.find_element(By.ID, 'password').send_keys('')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text != 'Тестов Тест'

#13 Негативный тест-кейс: авторизация по кнопке "логин" с некорректным  полем "логин"

def test_homepage_13(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('test_login')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'
    time.sleep(3)

#14 Негативный тест-кейс: авторизация по кнопке "логин" с некорректным полем "пароль"

def test_homepage_14(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_login)
    pytest_driver.find_element(By.ID, 'password').send_keys('password')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text != 'Тестов Тест'
    time.sleep(3)

#15 Негативный тест-кейс: авторизация по кнопке "логин"  с пустым полем "пароль"

def test_homepage_15(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_login)
    pytest_driver.find_element(By.ID, 'password').send_keys('')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text != 'Тестов Тест'
    time.sleep(3)


# 16 Негативный тест-кейс: авторизация по кнопке "логин" с некорректным полем "пароль"

def test_homepage_16(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_login)
    pytest_driver.find_element(By.ID, 'password').send_keys('password')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text != 'Тестов Тест'
    time.sleep(3)

# 17 Негативный тест-кейс: авторизация по кнопке "лицевой счет"  с некорректным лс

def test_homepage_17(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('12345')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text == 'Тестов Тест'
    time.sleep(3)

# 18 Негативный тест-кейс: авторизация по кнопке "лицевой счет"  с некорректным полем "пароль"

def test_homepage_18(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_ls)
    pytest_driver.find_element(By.ID, 'password').send_keys('password')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2'). text == 'Тестов Тест'
    time.sleep(3)

# 19 Негативный тест-кейс: авторизация по кнопке "лицевой счет"  с пустым полем "лицевой счет"

def test_homepage_19(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest_driver.find_element(By.ID, 'username').send_keys('')
    pytest_driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text == 'Тестов Тест'
    time.sleep(3)


# 20 Негативный тест-кейс: авторизация по кнопке "лицевой счет"  с пустым полем "пароль"

def test_homepage_20(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest_driver.find_element(By.ID, 'username').send_keys(valid_ls)
    pytest_driver.find_element(By.ID, 'password').send_keys('')
    pytest_driver.find_element(By.ID, 'kc-login').click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text == 'Тестов Тест'
    time.sleep(3)
