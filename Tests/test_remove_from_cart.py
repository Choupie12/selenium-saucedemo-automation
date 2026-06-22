from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

# Login
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add product
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Remove product
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

# Verify cart badge disappeared
try:
    driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    badge_exists = True
except NoSuchElementException:
    badge_exists = False

assert badge_exists == False

print("Product successfully removed from cart")

time.sleep(5)

driver.quit()