import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_invalid_login(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    submit = browser.find_element(By.ID, "submit")


    username.send_keys("wrong_user")
    password.send_keys("wrong_password")
    submit.click()


    try:
        assert "Your username is invalid!" in browser.page_source
    except AssertionError:
        browser.save_screenshot("../screenshots/login_failed2.png")
        raise
