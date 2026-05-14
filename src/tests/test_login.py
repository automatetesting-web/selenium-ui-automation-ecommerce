import pytest
from pages.login_page import LoginPage
from config.settings import LOGIN_EMAIL, LOGIN_PASSWORD
from locators.login_locators import LoginPageLocators

@pytest.mark.smoke
def test_user_can_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.go_to_login()
    login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert login_page.is_logged_in(), "User should be logged in successfully"

@pytest.mark.regression
def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.go_to_login()
    login_page.login(LOGIN_EMAIL, "wrongpassword")
    error = login_page.get_login_error()
    assert "incorrect" in error.lower()

@pytest.mark.regression
def test_user_can_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.go_to_login()
    login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert login_page.is_logged_in()
    login_page.logout()
    assert login_page.is_visible(LoginPageLocators.SIGNUP_LOGIN_BUTTON)