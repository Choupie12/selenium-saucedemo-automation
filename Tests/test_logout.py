from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Login
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Ouvrir le menu
driver.find_element(By.ID, "react-burger-menu-btn").click()

time.sleep(5)

# Logout
driver.find_element(By.ID, "logout_sidebar_link").click()

# Vérification
login_button = driver.find_element(By.ID, "login-button")

assert login_button.is_displayed()

print("Logout successful")

time.sleep(10)

driver.quit()