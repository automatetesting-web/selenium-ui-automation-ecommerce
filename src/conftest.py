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
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot("failure.png")
