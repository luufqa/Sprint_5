from selenium.webdriver.common.by import By
import locators


class TestConstructorElements:


# работают переходы к разделам: Соусы
    def test_check_constructor_element_sauces(self, driver):

        # кликаем по кнопкам внутри конструктора и записываем их измененные классы
        driver.find_element(By.XPATH, locators.sauces_element).click()
        sauces = driver.find_element(By.XPATH, locators.sauces_after_click).text
        assert sauces == 'Соусы'
        driver.find_element(By.XPATH, locators.fillings_element).click()
        fillings = driver.find_element(By.XPATH, locators.fillings_after_click).text

        driver.find_element(By.XPATH, locators.breads_element).click()
        breads = driver.find_element(By.XPATH, locators.breads_after_click).text
        # ожидаем, что список прокликанных кнопок в меню будет соответствовать
        # если успешно - значит классы изменились
        assert [sauces, fillings, breads] == ['Соусы', 'Начинки', 'Булки']
