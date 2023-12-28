from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


# переход по клику на «Конструктор» и на логотип Stellar Burgers
def test_step_jump_contructor_logo_in_profile():
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    # вводим существующий адрес почты аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(
        "luufqa@gmail.com")
    # вводим существующий пароль аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("3607833465")
    time.sleep(2)
    # кликаем по кнопке 'Войти'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()
    time.sleep(2)
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    time.sleep(2)
    # кликаем по логотипу
    driver.find_element(By.XPATH, ".//*[name()='svg' and @viewBox='0 0 290 50']").click()
    time.sleep(2)
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    time.sleep(2)
    # кликаем по кнопке 'Конструктор'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Конструктор')]").click()
    # проверяем наличие кнопки 'Оформить заказ' после переходов
    button_in_inside_profile = driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").text
    # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
    assert button_in_inside_profile == 'Оформить заказ'
    # завершаем работу
    driver.quit()
