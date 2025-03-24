import pytest
from selenium import webdriver
from faker import Faker

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def fake():
    return Faker()