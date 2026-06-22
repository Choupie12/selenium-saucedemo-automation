from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

title = driver.find_element(By.CLASS_NAME, "title").text

print("Titre trouvé :", title)

assert title == "Products"

time.sleep(30)

driver.quit()