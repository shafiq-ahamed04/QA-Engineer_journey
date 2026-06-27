#for loop

for i in range(5):
    print(i)

#while loop

count = 1

while count < 6:
    print(count)
    count +=1

#break

for i in range(5):
    if i == 3:
        break
    print(i)
#continue

for i in range(10):
    if i == 7:
        continue
    print(i)

#nested loop

browsers = ["Chrome", "Firefox"]
test_case = ["Login", "Search", "Checkout"]

for browser in browsers:
    for test in test_case:
        print(browser, "->", test)
        
