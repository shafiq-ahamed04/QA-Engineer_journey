DAY 32 — PYTEST INTRODUCTION

What I Learned:

Pytest is a Python testing framework used to run, manage, and report automated tests.

Selenium:
- Controls the browser.
- Performs browser actions.

Pytest:
- Runs the tests.
- Verifies results using assertions.
- Shows PASS/FAIL results.

Install Pytest:

pip install pytest

First Test:

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

Run Tests:

pytest test_day27_pytest.py

Important:

Pytest discovers test files/functions using naming conventions such as:
- test_*.py
- *_test.py

A test function normally starts with:
def test_...

Save as:

test_day27_pytest.py

Commit to GitHub

Time: 2 hours