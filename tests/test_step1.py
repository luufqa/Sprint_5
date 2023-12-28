from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


# переход по клику на «Личный кабинет»
def test_step_jump_in_auth_second_button():
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
    # кликаем по кнопке 'Личный Кабинет', чтобы открыть профиль пользователя
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()

    # ожидаем, что откроется профиль
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    # завершаем работу
    driver.quit()
