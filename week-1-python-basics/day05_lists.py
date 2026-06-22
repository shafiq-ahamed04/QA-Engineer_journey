browser = ["chrome", "firefox"]
browser.append("Edge")
print(browser)
browser.remove("firefox")
print(browser)
browser.sort()
print(browser)
browser.append("brave")
browser.sort()
print(browser)
for browsers in browser:
    print(browsers)
    