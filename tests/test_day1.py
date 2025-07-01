from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_day1():
    
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(3)
    assert "Products" in driver.page_source
    print("Login successful and on the Products page.")
    driver.quit()