import requests 
import pytest

def test_get_post_1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json() ["id"] == 1


def test_get_post_2():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2
