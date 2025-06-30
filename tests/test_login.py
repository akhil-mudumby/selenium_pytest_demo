from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_login():
    service = Service("D:\\selenium_pytest_demo\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    assert driver.current_url == "https://automationexercise.com/"
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    element.click()
    message = driver.find_element(By.XPATH, "//h2[normalize-space()='Login to your account']").text
    assert message == "Login to your account"
    user_box = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
    user_box.send_keys("akhil.mudumby@gmail.com")
    password_box = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_box.send_keys("Akhil78480")
    password_box.submit()
    login_message = driver.find_element(By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']").text
    assert login_message == "Your email or password is incorrect!"

    time.sleep(3)

    driver.quit()