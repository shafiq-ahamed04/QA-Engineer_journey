import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_form(browser):
    browser.get("https://demoqa.com/automation-practice-form")

    firstname = browser.find_element(By.ID, "firstName").send_keys("Shafiq")
    lastname = browser.find_element(By.ID, "lastName").send_keys("Ahamed")
    email = browser.find_element(By.ID, "userEmail").send_keys("ssa123@gmail.com")
    gender = browser.find_element(By.ID , "gender-radio-1")
    mobile = browser.find_element(By.ID, "userNumber").send_keys("5285269874")
    browser.execute_script("arguments[0].click();" , gender)
    hobbies = browser.find_element(By.ID,"hobbies-checkbox-2")
    browser.execute_script("arguments[0].click();", hobbies)
    address = browser.find_element(By.ID, "currentAddress").send_keys("sholapuram")

    submit = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].click();", submit)

    assert "Thanks for submitting the form" in browser.page_source

    print("Title: ", browser.title)
    print("link: ", browser.current_url)