# week - 04
# Selenium


1.What is selenium:
    It is an Tool used to Control the Web browsers, Because, We need test using browser without human clicking.

Step-1 -> Install selenium and verify it (pip install selenium & selenium --version)
step-2 -> Install chrome - dont do it manually, newer verdions of selenium do it by itself.
step-3 -> create file start program

2.Example program:
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()

        Line-01 -> Imports the browser controller itself
        Line-02 -> open Chrome Browser
        Line-03 -> get into the URL that entered inside the parameter
        Line 04 -> print the webpage title
        Line 05 -> close the chrome completly and stops every actions

3.what happens Internally:
    Python -> Selenium -> Chrome Drivers -> Chrome Browsers -> Google Opens -> Closed

4.Real company examples:
    Suppose, Amazon tester has 200 testcases, if we do manually , the tester wants to click login buttom for 200 times
Automation we wrote script to automate the testcases and it will handle it.




