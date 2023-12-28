from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


# вход через кнопку в форме восстановления пароля
def test_auth_in_second_button_from_restore():
    # кликаем по кнопке 'Личный Кабинет'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
    # кликаем по кнопке 'Восстановить пароль'
    driver.find_element(By.XPATH, ".//a[contains(text(), 'Восстановить пароль')]").click()
    # кликаем по кнопке 'Войти'
    driver.find_element(By.XPATH, ".//a[contains(text(), 'Войти')]").click()
    # вводим существующий адрес почты аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(
        "luufqa@gmail.com")
    # вводим существующий пароль аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("3607833465")
    time.sleep(2)
    # кликаем по кнопке 'Войти'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()
    time.sleep(2)
    # проверяем наличие кнопки 'Оформить заказ' после авторизации
    button_in_inside_profile = driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").text
    # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
    assert button_in_inside_profile == 'Оформить заказ'
    # завершаем работу
    driver.quit()
