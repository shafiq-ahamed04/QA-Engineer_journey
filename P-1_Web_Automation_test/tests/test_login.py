import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_login(browser):
    browser.get("https://demoqa.com/login")

    username =  browser.find_element(By.ID, "userName").send_keys("testuser")
    password = browser.find_element(By.ID, "password").send_keys("testpass")

    button = browser.find_element(By.ID, "login").click()

    print(browser.current_url)
    print(browser.title)
    print(browser.page_source)