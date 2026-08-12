import pytest
import requests

def test_post():
    data = {
        "title": "QA",
        "body" : "hello"
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)


    assert response.json()
    assert response.json() ["title"] == "QA"
    assert response.status_code == 201
    

    
