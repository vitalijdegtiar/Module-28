import pytest
from selenium import webdriver

# используется во всей сессии
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()