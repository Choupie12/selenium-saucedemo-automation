from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Ajouter le premier produit
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Vérifier le compteur du panier
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

print("Nombre d'articles :", cart_badge)

assert cart_badge == "1"

time.sleep(30)

driver.quit()