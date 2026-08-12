DAY 35 — API TESTING WITH REQUESTS

What I Learned:

API stands for Application Programming Interface.

An API acts as a communication bridge between applications and the server.

QA engineers can test APIs directly without depending only on the UI.

Install Requests:

pip install requests

Import:

import requests

GET Request:

GET is used to get/retrieve data from the server.

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print("Status:", response.status_code)
print("Data:", response.json())

POST Request:

POST is used to send data to the server.

data = {
    "title": "Test",
    "body": "Content"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print("Posted:", response.status_code)

Status Codes:

200 → Successful request
201 → Resource created
404 → Resource not found

response.json():

Converts the JSON response into a Python dictionary-like object so we can access values using keys.

Example:

data = response.json()

print(data["id"])
print(data["title"])

Save as:

day30_api_testing.py

Commit to GitHub

Time: 2-3 hours