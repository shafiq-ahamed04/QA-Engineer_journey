from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")
wait = WebDriverWait(driver,10)
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("shafiq")

print("explicit waits  successfully")

input("Press Enter to Close...")

driver.quit()