# week - 04
# Day - 30 - Element Actions

1.why do we need element actions?
    Imagine a real user, they dont stop after lookingat the textbox, they type clicks, reads.
Thats exactly this part. let see in detail

2.The Four Actions:

(1)send_keys():
    it is used to type.
ex: 
    search = driver.find_elements(By.NAME,"q")
    search.send_keys("python)
-> exactly like using keybord

(2)clear:
    it clears the text , that exist already.
ex:
    shafiq - already there
    raj - you need
    clear()
    now raj

(3)click:
    like clicking a mouse.
ex:
    login_button.click()
-> clicks the login button presented in the webpage

(4)text():
    It prints the text , in the text formant
ex:
    print (title.text)
-> prints the title of the webpage.

3.Real Company Flow:
    suppose,if test case says "login with valid credentials.
now,
    Manual tester:
        open website -> typer username -> type password -> click enter -> verify it
    Automation tester:
        username.send_keys()
        password.send_keys()
        button.click()
        print(message.text)
    and now , verifies with the message displayed. Exactly same, but method is different.
    