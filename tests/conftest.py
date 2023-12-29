import pytest
from selenium import webdriver

# !!! Не пониманию, почему тестовые функции не принимают driver из conftest HELP !!! #
# @pytest.mark.usefixtures("setup") - пытался подтянуть conftest
@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver

# !!! Не пониманию, почему тестовые функции не принимают driver из conftest HELP !!! #
# @pytest.mark.usefixtures("setup") - пытался подтянуть conftest
