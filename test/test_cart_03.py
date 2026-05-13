from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

## ESTILO PRUEBAS E2E ## 

def test_carrito(login_in_driver):
    driver = login_in_driver

    #Agrego producto a carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    #Extrae cantidad del carrito
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_carrito.text == "1", "El producto no se agrego correctamente"

    #Obtener nombre del primer producto
    nom_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #Producto del carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #Obtener nombre del procto del carrito
    item_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #Comparar nombres
    assert item_carrito == nom_producto, "Los nombres de los productos no coiciden"

