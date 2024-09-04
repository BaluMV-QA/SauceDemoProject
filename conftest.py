import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.yield_fixture
def log_on_failure(request):
    """
    To capture the screenshot of failed tests
    With the help of allure attach() to attach the screenshot in the report
    """
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to set up and tear down the WebDriver instance.
    """
    # driver as global variable to use it in the log_on_failure()
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
