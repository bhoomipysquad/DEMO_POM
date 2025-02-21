import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
        time.sleep(2)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(3)

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
