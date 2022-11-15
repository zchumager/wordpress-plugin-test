import pytest
from utils.webdriver import driver


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_wordpress_plugin(driver):
    driver.get("https://www.google.com/")
