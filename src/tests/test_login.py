from pages.login_page import LoginPage
from config.settings import LOGIN_EMAIL, LOGIN_PASSWORD


def test_user_can_login_with_valid_credentials(driver):
    """
    Verify that a user can log in with valid credentials.
    """

    login_page = LoginPage(driver)

    login_page.open()
    login_page.go_to_login()
    login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)

    assert login_page.is_logged_in(), "User should be logged in successfully"
