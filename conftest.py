import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdrivermanager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    # Set up the WebDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
