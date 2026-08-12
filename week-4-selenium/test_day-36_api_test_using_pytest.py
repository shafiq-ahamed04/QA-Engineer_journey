import requests

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response2 = requests.post("https://jsonplaceholder.typicode.com/posts")

def test_1():
    assert response1.status_code == 200

def test_2():
    assert response1.json()["id"] == 1

def test_3():
    assert response2.status_code == 201

def test_4():
    assert response1.elapsed.total_seconds() < 2
    assert response2.elapsed.total_seconds() < 2


 