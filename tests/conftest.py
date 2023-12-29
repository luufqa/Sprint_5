from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(20)
    return driver
