import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser name", action="store", default="chrome", help="Choose browser: chrome")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--browser name should be chrome")
    yield browser
    print("\nquit browser..")
    browser.quit()