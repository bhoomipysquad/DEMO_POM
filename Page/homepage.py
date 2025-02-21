import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.logout_button = (By.XPATH,'//*[@id="logout_sidebar_link"]')
        self.click_menu = (By.XPATH,'//*[@id="react-burger-menu-btn"]')

    def get_inventory_items(self):
        return self.driver.find_elements(*self.inventory_items)

    def click_logout(self):
        self.driver.find_element(*self.click_menu).click()
        time.sleep(3)
        self.driver.find_element(*self.logout_button).click()
