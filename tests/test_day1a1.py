from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_day1p2():
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Welcome to the Secure Area. When you are done click logout below." in driver.page_source
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='button secondary radius']").click()
    time.sleep(3)

    driver.quit()
