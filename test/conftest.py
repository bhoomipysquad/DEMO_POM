import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    # Teardown
    driver.quit()
