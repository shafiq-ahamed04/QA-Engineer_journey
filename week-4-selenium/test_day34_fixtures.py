import pytest 
from selenium import webdriver

@pytest.fixture
def qa():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

def test_amazon(qa):
    qa.get("https://www.amazon.in")
    print("Title: ", qa.title)

def test_google(qa):
    qa.get("https://www.google.com")
    print("Title: ", qa.title)

def test_github(qa):
    qa.get("https://www.github.com")
    print("Title: ", qa.title)
