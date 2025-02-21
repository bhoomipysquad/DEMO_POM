import pytest
from Page.LoginPage import   LoginPage
from Page.homepage import HomePage


@pytest.mark.parametrize("username,password,expected_result", [
    ("standard_user", "secret_sauce", "Home Page"),
    ("locked_out_user", "secret_sauce", "Error Message"),
    ("problem_user", "secret_sauce", "Home Page"),
    ("performance_glitch_user", "secret_sauce", "Home Page")
])
def test_login(username, password, expected_result, driver):
    # Initialize the Login Page
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Check if login is successful
    if expected_result == "Home Page":
        home_page = HomePage(driver)
        assert len(home_page.get_inventory_items()) > 0, "Home page not loaded correctly"
    else:
        error_message = login_page.get_error_message()
        assert error_message == "Epic sadface: Sorry, this user has been locked out.", f"Unexpected error message: {error_message}"
