import pytest 
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

def test_1():
    assert response.status_code == 200

def test_2():
    assert data[id] == 1

def test_3():
    assert "title" in data 

def test_4():
    assert response.elapsed.total_seconds() < 2