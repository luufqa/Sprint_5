from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
import pytest

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# создаем случаеное Имя и Фамилию для почты
First_name = ['Alexey', 'Andrew', 'Sergey', 'Mark', 'Robert']
Last_name = ['Pshenitsyn', 'Romanenko', 'Semenov', 'Ivanov']
random_First_name = random.choice(First_name)
random_Last_name = random.choice(Last_name)

# создаем случайный адрес почты
random_email = f"{random_First_name}{random_Last_name}1{random.randint(100, 999)}@yandex.ru"


# проверка регистрации, три случая

# тест №1 - убеждаемся, что с уже ранее зарегистрированным пользователем, повторном регистрация не проходит
@pytest.mark.parametrize("login, email, password, expected_result",
                         [('luufqa', 'luufqa@gmail.com', '3607833465',
                           'Такой пользователь уже существует')])
def test_reg_with_already_user(login, email, password, expected_result):
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    # кликаем по кнопке 'Зарегистрироваться'
    driver.find_element(By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]").click()
    # передаем логин
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
    # передаем почту
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)
    # передаем пароль
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
    # кликаем по кнопке 'Зарегистрироваться'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
    time.sleep(3)
    # ожидаем, что появится ошибка 'Такой пользователь уже существует'
    res = driver.find_element(By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")
    assert expected_result == res.text


# тест №2 - убеждаемся, что вводе некорректного пароля, появляется тултип "Некорректный пароль"
@pytest.mark.parametrize("login, email, password, expected_result",
                         [('luufqa', 'luufqa@gmail.com', '156', "Некорректный пароль")])
def test_reg_with_uncorrect_password(login, email, password, expected_result):
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    # кликаем по кнопке 'Зарегистрироваться'
    driver.find_element(By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]").click()
    # передаем логин
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
    # передаем почту
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)
    # передаем пароль
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
    # кликаем по кнопке 'Зарегистрироваться'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
    time.sleep(3)
    # ожидаем, что появится ошибка 'Некорректный пароль'
    res = driver.find_element(By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")
    assert expected_result == res.text


# тест №3 - убеждаемся, что с корректными данными открывается нужный раздел и вход выполнен
@pytest.mark.parametrize("login, email, password, expected_result",
                         [('1', random_email, '1561232', "https://stellarburgers.nomoreparties.site/login")])
def test_reg_with_correct_new_account(login, email, password, expected_result):
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    # кликаем по кнопке 'Зарегистрироваться'
    driver.find_element(By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]").click()
    # передаем логин
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
    # передаем почту
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)
    # передаем пароль
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
    # кликаем по кнопке 'Зарегистрироваться'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
    time.sleep(3)
    # ожидаем, что вход будет выполнен
    assert expected_result == driver.current_url
