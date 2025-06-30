from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_google_search():
    service = Service("D:\\selenium_pytest_demo\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.google.com")
    time.sleep(1)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium with Python")
    search_box.submit()

    time.sleep(3)

    driver.quit()
