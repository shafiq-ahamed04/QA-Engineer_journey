import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def login_automation():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

def test_login(login_automation):
    login_automation.get("https://practicetestautomation.com/practice-test-login/")
    login_automation.find_element(By.ID, "username").send_keys("student")
    login_automation.find_element(By.ID, "password").send_keys("Password123")
    login_automation.find_element(By.ID, "submit").click()

    assert "Logged In Successfully" in login_automation.page_source
    





        