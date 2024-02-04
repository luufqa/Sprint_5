import pytest
from selenium.webdriver.common.by import By
import random
from faker import Faker
import locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# создаем случаеное Имя и Фамилию для почты
name = Faker(['en_US']).name().replace(' ', '')

# создаем случаеную учетку
number_pass = f"{random.randint(100000, 999999)}"
number_for_email = f"1{random.randint(100, 999)}"
random_email = f"{name}1{number_for_email}@yandex.ru"


class TestRegCases:
    # проверка регистрации, три случая

    # тест №1 - убеждаемся, что с уже ранее зарегистрированным пользователем, повторном регистрация не проходит
    @pytest.mark.parametrize("login, email, password, expected_result",
                             [('luufqa', 'luufqa@gmail.com', '3607833465',
                               'Такой пользователь уже существует'),
                              ('i220493', 'i220493@yandex.ru', '3607833465', 'Такой пользователь уже существует')])
    def test_reg_with_already_user(self, login, email, password, expected_result, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Зарегистрироваться'
        driver.find_element(By.XPATH, locators.register_button).click()
        # передаем логин
        driver.find_element(By.XPATH, locators.field_register_login).send_keys(login)
        # передаем почту
        driver.find_element(By.XPATH, locators.field_register_email).send_keys(email)
        # передаем пароль
        driver.find_element(By.XPATH, locators.field_register_password).send_keys(password)
        # кликаем по кнопке 'Зарегистрироваться'
        driver.find_element(By.XPATH, locators.register_button_second).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            locators.tooltip_message_user))
        )
        # ожидаем, что появится ошибка 'Такой пользователь уже существует'
        res = driver.find_element(By.XPATH, locators.tooltip_message_user)
        assert expected_result == res.text

    # тест №2 - убеждаемся, что вводе некорректного пароля, появляется тултип "Некорректный пароль"
    @pytest.mark.parametrize("login, email, password, expected_result",
                             [('luufqa', 'luufqa@gmail.com', '156', "Некорректный пароль"),
                              ('luufqa', 'luufqa@gmail.com', '1', "Некорректный пароль")])
    def test_reg_with_uncorrect_password(self, login, email, password, expected_result, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Зарегистрироваться'
        driver.find_element(By.XPATH, locators.register_button).click()

        # передаем логин
        driver.find_element(By.XPATH, locators.field_register_login).send_keys(login)

        # передаем почту
        driver.find_element(By.XPATH, locators.field_register_email).send_keys(email)

        # передаем пароль
        driver.find_element(By.XPATH, locators.field_register_password).send_keys(password)
        # кликаем по кнопке 'Зарегистрироваться'
        driver.find_element(By.XPATH, locators.register_button_second).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            locators.tooltip_message_pass))
        )
        # ожидаем, что появится ошибка 'Некорректный пароль'
        res = driver.find_element(By.XPATH, locators.tooltip_message_pass)
        assert expected_result == res.text

    # тест №3 - убеждаемся, что с корректными данными регистрация проходит
    def test_reg_with_correct_new_account(self, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Зарегистрироваться'
        driver.find_element(By.XPATH, locators.register_button).click()
        # передаем логин
        driver.find_element(By.XPATH, locators.field_register_login).send_keys(name)
        # передаем почту
        driver.find_element(By.XPATH, locators.field_register_email).send_keys(random_email)
        # передаем пароль
        driver.find_element(By.XPATH, locators.field_register_password).send_keys(number_pass)
        # кликаем по кнопке 'Зарегистрироваться'
        driver.find_element(By.XPATH, locators.register_button_second).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            locators.enter_profile_button_second))
        )
        # ожидаем, что вход будет выполнен
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url
