import pytest
from selenium import webdriver
from utils.login_pages import login

@pytest.fixture #Define configuracion para reutilizar en diferentes pruebas
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options = options)

    yield driver

    driver.quit() 

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver