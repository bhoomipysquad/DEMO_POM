from Page.homepage import HomePage


def test_inventory_items(driver):
    # After login, we should be on the home page
    home_page = HomePage(driver)
    inventory_items = home_page.get_inventory_items()
    assert len(inventory_items) > 0, "No inventory items found"


def test_logout(driver):
    # Logout from the home page
    home_page = HomePage(driver)
    home_page.click_logout()

    # Check that the user is redirected to the login page
    assert "login" in driver.current_url, "Logout failed"
