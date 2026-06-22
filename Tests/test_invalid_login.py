from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("wrong_password")

driver.find_element(By.ID, "login-button").click()

error_message = driver.find_element(By.TAG_NAME, "h3").text

print("Message trouvé :", error_message)

assert "Username and password do not match" in error_message

time.sleep(30)

driver.quit()