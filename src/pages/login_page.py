from core.base_page import BasePage
from locators.login_locators import LoginPageLocators
from config.settings import BASE_URL


class LoginPage(BasePage):

    def open(self):
        self.driver.get(BASE_URL)

    def go_to_login(self):
        self.click(LoginPageLocators.SIGNUP_LOGIN_BUTTON)

    def login(self, email, password):
        self.type(LoginPageLocators.EMAIL_INPUT, email)
        self.type(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.is_visible(LoginPageLocators.LOGGED_IN_LABEL)

    def logout(self):
        self.click(LoginPageLocators.LOGOUT_BUTTON)

    def get_login_error(self):
        return self.get_text(LoginPageLocators.LOGIN_ERROR_MESSAGE)