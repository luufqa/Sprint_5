from selenium.webdriver.common.by import By
import locators


class TestConstructorElements:


    # проверка перехода и изменение класса раздела: Соусы
    def test_check_constructor_element_sauces(self, driver):

        # кликаем по кнопкам внутри конструктора и записываем их измененные классы
        driver.find_element(By.XPATH, locators.sauces_element).click()
        sauces = driver.find_element(By.XPATH, locators.sauces_after_click).text
        assert sauces == 'Соусы'
