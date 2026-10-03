import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

def test_search(browser):
    browser.get("https://www.amazon.in/")

    search = browser.find_element(By.ID, "twotabsearchtextbox").send_keys("laptop")
    button = browser.find_element(By.XPATH, "//input[@type = 'submit']").click()

    assert "Results" in browser.page_source

    print("title", browser.title)
    print("link", browser.current_url)
