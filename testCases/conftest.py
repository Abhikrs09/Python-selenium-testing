import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.readProperties import ReadConfig

"""
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

"""

mode = ReadConfig.getApplicationMode()


# @pytest.fixture
# def setup(browser):
#     if mode == "non-headless":
#         if browser == "chrome":
#             driver = webdriver.Chrome()
#             print("********* launching Chrome Browser in non-headless Mode ***********")
#         elif browser == "firefox":
#             driver = webdriver.Firefox()
#             print("********* launching Firefox Browser in non-headless Mode ***********")
#     elif mode == "headless":
#         if browser == "chrome":
#             options = Options()
#             options.headless = True
#             driver = webdriver.Chrome()
#             print("********* launching Chrome Browser in headless Mode ***********")
#         elif browser == "firefox":
#             options = Options()
#             options.headless = True
#             driver = webdriver.Firefox()
#             print("********* launching Firefox Browser in non-headless Mode ***********")
#     return driver


@pytest.fixture(scope="function")
def setup(browser):
    driver = None  # Initialize driver

    # Check the mode and browser type
    if mode == "non-headless":
        if browser == "chrome":
            driver = webdriver.Chrome()
            print("********* launching Chrome Browser in non-headless Mode ***********")
        elif browser == "firefox":
            driver = webdriver.Firefox()
            print("********* launching Firefox Browser in non-headless Mode ***********")
    elif mode == "headless":
        if browser == "chrome":
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            print("********* launching Chrome Browser in headless Mode ***********")
        elif browser == "firefox":
            options = FirefoxOptions()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            print("********* launching Firefox Browser in headless Mode ***********")

    # Navigate to the application URL and maximize the window
    driver.get(ReadConfig.getApplicationUrl())
    driver.maximize_window()

    yield driver  # Yield the driver for use in tests

    if driver:
        driver.quit()  # Ensure the driver is closed after tests

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

