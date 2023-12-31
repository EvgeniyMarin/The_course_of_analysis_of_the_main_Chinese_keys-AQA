import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver_browser = webdriver.Chrome()
    yield driver_browser
    driver_browser.quit()

