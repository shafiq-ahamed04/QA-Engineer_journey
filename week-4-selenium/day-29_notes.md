# week - 04
# finding web elements using locators

1.What is web element?
    Everything we see on the webpage is element. (texts, images, logos, links etc..)
Selenium must identify the correct one we need to take action.

2.what is find elements?
    It tells selenium to locate specific element on the webpage. Without this,
selenium cant do anything.
 
    think of it like this:
        open browser -> open website -> find search box -> Type texts

3.Why do we use By.
    Look at Google, There are many elements and how do we identify the one that we need?
for this, selenium Provides different strategies.

    Locator - 01: By.ID
        -> element = driver.find_element(By.ID, "username")
    Meaning -> Find elements whose ID is Username. 
ID should be unique on page, so They are the best locators.

    Locator - 02: By.NAME
        -> search = driver.find_elements(By.NAME='q')
    Meaning -> Find element whose name is q
NAME should be same as ID , but it follows the attribute given on HTML

    Locator - 03 and 04: 
      By.CSS_SELECTOR
      By.XPATH

        ->These two are same but with, different code, but the purpose is same. Xpath is powerful,
    but it is fragile and long .

refer the code in file(day-29_selenium_locatotrs.py) for better understanding.

4.Real company Example:
    find username textbox -> enter username -> same for password -> click login

so, the real QA engineers , 1st inspect the html, then they choose locators need to use .