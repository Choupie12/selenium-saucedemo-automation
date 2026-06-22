from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com")

# Login with locked user
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Error message
error_message = driver.find_element(
    By.CSS_SELECTOR,
    "[data-test='error']"
).text

print("Error message:", error_message)

assert "locked out" in error_message.lower()

time.sleep(5)

driver.quit()