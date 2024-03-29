from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import accounts
import locators


class TestAuthCases:
    # вход по кнопке «Войти в аккаунт» на главной

    def test_auth_in_first_login_button(self, driver):
        # кликаем по кнопке 'Войти в аккаунт'
        driver.find_element(By.XPATH, locators.first_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(accounts.testing_acc_email)
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(accounts.testing_acc_pass)
        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()
        # проверяем наличие кнопки 'Оформить заказ' после авторизации
        button_in_inside_profile = driver.find_element(By.XPATH, locators.get_order_button).text
        # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
        assert button_in_inside_profile == 'Оформить заказ'

    # вход через кнопку «Личный кабинет»
    def test_auth_in_second_login_button(self, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(accounts.testing_acc_email)
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(accounts.testing_acc_pass)

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # проверяем наличие кнопки 'Оформить заказ' после авторизации
        button_in_inside_profile = driver.find_element(By.XPATH, locators.get_order_button).text
        # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
        assert button_in_inside_profile == 'Оформить заказ'

    # вход через кнопку в форме регистрации
    def test_auth_in_second_login_button_from_reg(self, driver):
        # кликаем по кнопке 'Личный Кабинет'

        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Зарегистрироваться'

        driver.find_element(By.XPATH, locators.register_button).click()

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button).click()

        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(accounts.testing_acc_email)
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(accounts.testing_acc_pass)

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.get_order_button))
        )
        # проверяем наличие кнопки 'Оформить заказ' после авторизации
        button_in_inside_profile = driver.find_element(By.XPATH, locators.get_order_button).text
        # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
        assert button_in_inside_profile == 'Оформить заказ'

    # вход через кнопку в форме восстановления пароля
    def test_auth_in_second_login_button_from_restore(self, driver):
        # кликаем по кнопке 'Личный Кабинет

        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Восстановить пароль'

        driver.find_element(By.XPATH, locators.restore_button).click()
        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button).click()
        # вводим существующий адрес почты аккаунта

        driver.find_element(By.XPATH, locators.field_email).send_keys(accounts.testing_acc_email)
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(accounts.testing_acc_pass)

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.get_order_button))
        )
        # проверяем наличие кнопки 'Оформить заказ' после авторизации
        button_in_inside_profile = driver.find_element(By.XPATH, locators.get_order_button).text
        # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
        assert button_in_inside_profile == 'Оформить заказ'
