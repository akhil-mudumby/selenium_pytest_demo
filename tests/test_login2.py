import time
from pages.login_page import LoginPage

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    time.sleep(2)
    assert "Products" in driver.page_source
    