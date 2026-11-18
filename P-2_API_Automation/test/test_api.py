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

import requests


def test_post_create():
    data = {
        "title": "Test",
        "body": "Content"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )

    assert response.status_code == 201


def test_get_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_invalid_endpoint():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/invalid"
    )

    assert response.status_code == 404