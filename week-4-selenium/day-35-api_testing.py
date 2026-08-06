import pytest
import requests

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data ={
    "title" : "hello",
    "body" : "python"
}
response2 = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)

def statuscode1():
    print("Status_Code: ", response1.status_code)
    if response1.status_code == 400:
        print("verified")
    else:
        print("Wrong status code")

def statuscode2():
    print("Status_Code: ", response2.status_code)
    if response2.status_code == 201:
        print("verified")
    else:
        print("Wrong status code")

def verify_results():
    if response1.status_code == 200 and response2.status_code == 201:
        print("API Testing Sucesssful")
    else:
        print("API Test Failed")

statuscode1()
statuscode2()
verify_results()










