from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


# выход по кнопке «Выйти» в личном кабинете
def test_check_user_logout():
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
    # кликаем по кнопке 'Выход', чтобы выйти из профиля
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Выход')]").click()
    time.sleep(2)

    # ожидаем, что выход из профиля выполняется корректно
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    # завершаем работу
    driver.quit()
