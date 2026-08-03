from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://amazon.in")
print("Title: ", driver.title)
print("URL: ", driver.current_url)

driver.close()