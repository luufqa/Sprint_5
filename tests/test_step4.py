from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")


# работают переходы к разделам: Булки, Соусы, Начинки
def test_step_jump_inside_contructor_menu():
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
    # кликаем по кнопке 'Конструктор'
    driver.find_element(By.XPATH, ".//p[contains(text(), 'Конструктор')]").click()
    time.sleep(2)
    # кликаем по кнопкам внутри конструктора и записываем их наименования в список
    el1 = driver.find_element(By.XPATH, ".//span[contains(text(), 'Соусы')]")
    el1.click()
    time.sleep(1)
    el2 = driver.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]")
    el2.click()
    time.sleep(1)
    el3 = driver.find_element(By.XPATH, ".//span[contains(text(), 'Булки')]")
    el3.click()
    time.sleep(1)
    # помещаем прокликанные заголовки в список
    li = [el1.text, el2.text, el3.text]
    li.sort()
    # ожидаем, что список прокликанных список в меню будет соответствовать
    assert ['Булки', 'Начинки', 'Соусы'] == li
    # завершаем работу
    driver.quit()
