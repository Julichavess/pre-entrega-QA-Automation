from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

'''
def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
'''

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver 

def test_invent_title(driver_logged):
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "El titulo de la pestaña no es correcto"

def test_visible_products(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0 

def test_ui(driver_logged):
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed(), "No se encuentra el menu" #Saber si estan visibles en la pantalla 
    assert filtro.is_displayed(), "no se encuentra el filtro"