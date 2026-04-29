from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    All locators for Login / Signup page.
    """

    # Header
    SIGNUP_LOGIN_BUTTON = (By.LINK_TEXT, "Signup / Login")

    # Login form
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")

    # Logged-in state
    LOGGED_IN_LABEL = (
        By.XPATH,
        "//a[contains(text(),'Logged in as')]"
    )

    # Logout
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")

    # Error message
    LOGIN_ERROR_MESSAGE = (
        By.XPATH,
        "//p[text()='Your email or password is incorrect!']"
    )