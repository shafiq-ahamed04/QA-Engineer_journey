DAY 34 — PYTEST FIXTURES

What I Learned:

A fixture is a reusable section of code used for setup and teardown.

It helps avoid repeating the same setup and cleanup code for many tests.

@pytest.fixture:

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_google_title(browser):
    browser.get("https://www.google.com")
    assert browser.title == "Google"

Setup:
- Runs before the test.
- Example: Open browser.

Teardown:
- Runs after the test.
- Example: Close browser.

yield:

yield gives the browser to the test.

Flow:

Setup
↓
yield
↓
Test runs
↓
Fixture resumes
↓
Teardown

Without fixtures:

Every test needs its own setup and cleanup.

With fixtures:

One reusable setup/teardown can be used by many tests.

autouse=True:

@pytest.fixture(autouse=True)

Automatically uses the fixture without passing the fixture name into every test.

Run:

pytest test_day29_fixtures.py

Save as:

test_day29_fixtures.py

Commit to GitHub

Time: 2-3 hours