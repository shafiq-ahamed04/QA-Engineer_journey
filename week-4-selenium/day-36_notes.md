DAY 36 — API TESTING USING PYTEST

What I Learned:

Pytest can be combined with Requests to automatically test APIs.

Instead of manually checking the API output with print(), assertions verify whether the response is correct.

GET API Test:

import requests
import pytest

def test_get_api():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1

Status Code Assertion:

assert response.status_code == 200

This verifies that the API returned the expected status code.

Response Data Assertion:

assert response.json()["id"] == 1

This verifies that the response contains the expected data.

POST API Test:

def test_post_api():
    data = {
        "title": "Test"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )

    assert response.status_code == 201

Response Time Assertion:

assert response.elapsed.total_seconds() < 2

This verifies that the API responds within the expected time.

Important:

Status code alone is not enough.

An API can return 200 but still contain incorrect response data.

Example:

assert response.status_code == 200
assert response.json()["id"] == 1

Run:

pytest test_day31_api_assertions.py

Save as:

test_day31_api_assertions.py

Commit to GitHub

Week 4 Total Commits: 10 commits
Total So Far: 25 + 10 = 35 commits

Time: 2-3 hours