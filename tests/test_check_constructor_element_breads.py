from selenium.webdriver.common.by import By
import locators


class TestConstructorElements:

    # проверка перехода и изменение класса раздела: Булки
    def test_check_constructor_element_breads(self, driver):
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы
        driver.find_element(By.XPATH, locators.sauces_element).click()
        driver.find_element(By.XPATH, locators.breads_element).click()
        breads = driver.find_element(By.XPATH, locators.breads_after_click).text
        assert breads == 'Булки'
