from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Login
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add product
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
print("Product added")

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print("Cart opened")
time.sleep(3)
print(driver.current_url)

# Checkout
driver.find_element(By.ID, "checkout").click()
print("Checkout opened")

# Customer information
driver.find_element(By.ID, "first-name").send_keys("Felicienne")
print("First name entered")
driver.find_element(By.ID, "last-name").send_keys("Miezan")
print("Last name entered")
driver.find_element(By.ID, "postal-code").send_keys("75001")
print("Postal code entered")

driver.find_element(By.ID, "continue").click()
print("Continue clicked")

# Finish order
driver.find_element(By.ID, "finish").click()
print("Finish clicked")

# Verification
confirmation_message = driver.find_element(
    By.CLASS_NAME,
    "complete-header"
).text

print("Confirmation :", confirmation_message)

assert confirmation_message == "Thank you for your order!"

time.sleep(15)

driver.quit()