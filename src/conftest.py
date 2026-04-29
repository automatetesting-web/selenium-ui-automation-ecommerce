import pytest
from core.driver_factory import create_driver


@pytest.fixture
def driver():
    """
    Pytest fixture to provide a WebDriver instance to tests.
    """
    driver = create_driver()
    yield driver
    driver.quit()
    