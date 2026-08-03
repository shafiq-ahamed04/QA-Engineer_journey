from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

username = driver.find_element(By.ID, "userName")
username.send_keys("shafiq")

email = driver.find_element(By.ID, "userEmail")
email.send_keys("shafiq@gmail.com")

current_address = driver.find_element(By.ID, "currentAddress")
current_address.send_keys("Trichy")

permt_address = driver.find_element(By.ID, "permanentAddress")
permt_address.send_keys("Tamilnadu")

button = driver.find_element(By.ID, "submit")
button.click()

print("typed successfully")

input("Press Enter to Close...")
driver.quit()