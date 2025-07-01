from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_day1p2():
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert "Products" in driver.page_source
    print("Login successful and on the Products page")

    driver.quit()
