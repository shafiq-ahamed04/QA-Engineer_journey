import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("valid_user")
    driver.find_element(By.ID, "password").send_keys("valid_password")
    driver.find_element(By.CLASS_NAME, "radius").click()

    page_text = driver.page_source 
    assert "Dashboard" in page_text

    driver.quit()