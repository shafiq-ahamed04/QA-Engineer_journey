DAY 33 — PYTEST ASSERTIONS

What I Learned:

Assertions are verification statements used to check whether the actual result matches the expected result.

Equal:

assert 5 == 5

Not Equal:

assert 5 != 3

True:

assert True == True

False:

assert False == False

In:

assert 3 in [1, 2, 3, 4]

Assertions automatically produce PASS or FAIL in Pytest.

pytest.raises():

Used when we expect a specific exception to occur.

Example:

with pytest.raises(ValueError):
    ...

Important:

assert verifies a condition.

print() only displays a value in the terminal; it does not verify the expected result.

Run:

pytest test_day28_assertions.py

Save as:

test_day28_assertions.py

Commit to GitHub

Time: 2 hours