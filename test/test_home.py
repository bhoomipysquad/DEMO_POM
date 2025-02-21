from Page.LoginPage import LoginPage
from Page.homepage import HomePage


def test_inventory_items(driver):
    # After login, we should be on the home page
    login_page = LoginPage(driver)
    login_page.enter_username(username = "standard_user")
    login_page.enter_password(password = "secret_sauce")
    login_page.click_login()
    home_page = HomePage(driver)
    inventory_items = home_page.get_inventory_items()
    assert len(inventory_items) > 0, "No inventory items found"


def test_logout(driver):
    # Logout from the home page

    login_page = LoginPage(driver)
    login_page.enter_username(username = "standard_user")
    login_page.enter_password(password = "secret_sauce")
    login_page.click_login()
    home_page = HomePage(driver)
    home_page.click_logout()


    # Check that the user is redirected to the login page
    assert  driver.current_url == "https://www.saucedemo.com/"
