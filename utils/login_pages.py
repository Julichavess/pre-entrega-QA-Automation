from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver):
    driver.get("https://www.saucedemo.com/") # Defino el navegador

    #Ingreso usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    #Ingreso Password
    contra = driver.find_element(By.ID, "password")
    contra.send_keys("secret_sauce")

    #Apretar boton login RETURN -> BOTON ENTER
    #contra.send_keys(Keys.RETURN)

    #Ingreso boton login
    driver.find_element(By.ID, "login-button").click()

    
