import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_browser(browser):
    if browser == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())


@pytest.fixture
def driver(browser):
    instance = get_browser(browser)
    yield instance
    instance.quit()
