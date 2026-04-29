from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """
    BasePage provides reusable Selenium interactions.
    All Page Objects must inherit from this class.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        """
        Click an element after waiting for it to be clickable.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text, clear=True):
        """
        Type text into an input after waiting for visibility.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Return visible text from an element.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        """
        Check if an element is visible.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_attribute(self, locator, attribute):
        """
        Return an attribute value from an element.
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
