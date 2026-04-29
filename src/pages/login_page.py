from core.base_page import BasePage
from locators.login_locators import LoginPageLocators
from config.settings import BASE_URL


class LoginPage(BasePage):
    """
    Page Object for Login functionality.
    """

    def open(self):
        """
        Open the application home page.
        """
        self.driver.get(BASE_URL)

    def go_to_login(self):
        """
        Navigate to the Login / Signup page.
        """
        self.click(LoginPageLocators.SIGNUP_LOGIN_BUTTON)

    def login(self, email, password):
        """
        Log in using provided credentials.
        """
        self.type(LoginPageLocators.EMAIL_INPUT, email)
        self.type(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def is_logged_in(self):
        """
        Check if the user is logged in.
        """
        return self.is_visible(LoginPageLocators.LOGGED_IN_LABEL)

    def logout(self):
        """
        Log out the current user.
        """
        self.click(LoginPageLocators.LOGOUT_BUTTON)

    def get_login_error(self):
        """
        Return login error message text.
        """
        return self.get_text(LoginPageLocators.LOGIN_ERROR_MESSAGE)