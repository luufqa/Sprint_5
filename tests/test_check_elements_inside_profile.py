from selenium.webdriver.common.by import By
import locators
import accounts
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestElementsInsideProfile:
    # переход по клику на «Личный кабинет»
    def test_open_user_profile_in_auth_second_login_button(self, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(accounts.testing_acc_email)
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(accounts.testing_acc_pass)

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # кликаем по кнопке 'Личный Кабинет', чтобы открыть профиль пользователя
        driver.find_element(By.XPATH, locators.second_login_button).click()

        # ожидаем, что откроется профиль
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # выход по кнопке «Выйти» в личном кабинете
    def test_check_user_logout(self, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # вводим существующий адрес почты аккаунта
        driver.find_element(By.XPATH, locators.field_email).send_keys(accounts.testing_acc_email)
        # вводим существующий пароль аккаунта
        driver.find_element(By.XPATH, locators.field_password).send_keys(accounts.testing_acc_pass)

        # кликаем по кнопке 'Войти'
        driver.find_element(By.XPATH, locators.enter_profile_button_second).click()

        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Выход', чтобы выйти из профиля
        driver.find_element(By.XPATH, locators.logout_button).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            locators.enter_profile_button_second))
        )
        # ожидаем, что выход из профиля выполняется корректно
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # переход по клику на «Конструктор» и на логотип Stellar Burgers
    def test_check_click_for_elements_constructor_and_logo(self, driver):
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по логотипу
        driver.find_element(By.XPATH, locators.logo).click()
        # кликаем по кнопке 'Личный Кабинет'
        driver.find_element(By.XPATH, locators.second_login_button).click()
        # кликаем по кнопке 'Конструктор'
        driver.find_element(By.XPATH, locators.constructor_element).click()
        # проверяем наличие кнопки 'Оформить заказ' после переходов
        button_in_inside_profile = driver.find_element(By.XPATH, locators.first_login_button).text
        # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
        assert button_in_inside_profile == 'Войти в аккаунт'
