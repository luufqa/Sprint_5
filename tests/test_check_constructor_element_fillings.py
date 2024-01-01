from selenium.webdriver.common.by import By
import locators


class TestConstructorElements:

    # работают переходы к разделам: Начинки
    def test_check_constructor_element_fillings(self, driver):
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы
        driver.find_element(By.XPATH, locators.fillings_element).click()
        fillings = driver.find_element(By.XPATH, locators.fillings_after_click).text
        assert fillings == 'Начинки'
