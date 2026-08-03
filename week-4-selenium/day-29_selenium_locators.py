from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

element = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
print(element)

driver.quit()