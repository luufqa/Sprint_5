from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import locators


class TestElementsInsideProfile:
    # переход по клику на «Личный кабинет»
    def test_open_user_profile_in_auth_second_login_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(
            "luufqa@gmail.com")
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(
            "3607833465")

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # кликаем по кнопке 'Личный Кабинет', чтобы открыть профиль пользователя
        driver.find_element(By.XPATH, locators.second_login_button).click()

        # ожидаем, что откроется профиль
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # выход по кнопке «Выйти» в личном кабинете
    def test_check_user_logout(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(
            "luufqa@gmail.com")
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(
            "3607833465")

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Выход', чтобы выйти из профиля
        driver.find_element(By.XPATH, locators.logout_button).click()
        time.sleep(2)

        # ожидаем, что выход из профиля выполняется корректно
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    # переход по клику на «Конструктор» и на логотип Stellar Burgers
    def test_check_click_for_elements_constructor_and_logo(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(
            "luufqa@gmail.com")
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(
            "3607833465")

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()

        # кликаем по логотипу
        driver.find_element(By.XPATH, locators.logo).click()

        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()

        # кликаем по кнопке 'Конструктор'
        driver.find_element(By.XPATH, locators.constructor_element).click()
        # проверяем наличие кнопки 'Оформить заказ' после переходов
        button_in_inside_profile = driver.find_element(By.XPATH, locators.get_order_button).text
        # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
        assert button_in_inside_profile == 'Оформить заказ'
        driver.quit()

    # работают переходы к разделам: Булки, Соусы, Начинки
    def test_check_click_for_elements_inside_constructor_menu(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(
            "luufqa@gmail.com")
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(
            "3607833465")

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Конструктор'
        driver.find_element(By.XPATH, locators.constructor_element).click()

        # кликаем по кнопкам внутри конструктора и записываем их измененные классы
        driver.find_element(By.XPATH, locators.sauces_element).click()
        sauces = driver.find_element(By.XPATH, locators.sauces_after_click).text

        driver.find_element(By.XPATH, locators.fillings_element).click()
        fillings = driver.find_element(By.XPATH, locators.fillings_after_click).text

        driver.find_element(By.XPATH, locators.breads_element).click()
        breads = driver.find_element(By.XPATH, locators.breads_after_click).text
        # ожидаем, что список прокликанных кнопок в меню будет соответствовать
        # если успешно - значит классы изменились
        assert [sauces, fillings, breads] == ['Соусы', 'Начинки', 'Булки']

        driver.quit()
