from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


# вход по кнопке «Войти в аккаунт» на главной
def test_auth_in_first_button():
    # кликаем по кнопке 'Войти в аккаунт'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]").click()
    # вводим существующий адрес почты аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(
        "luufqa@gmail.com")
    # вводим существующий пароль аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("3607833465")
    # кликаем по кнопке 'Войти'
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()
    # проверяем наличие кнопки 'Оформить заказ' после авторизации
    button_in_inside_profile = driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").text
    # ожидаем, что откроется профиль и будет присутствовать кнопка 'Оформить заказ'
    assert button_in_inside_profile == 'Оформить заказ'
    # завершаем работу
    driver.quit()
