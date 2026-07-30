DAY 24 – BUG REPORTING

What is a Bug?

A bug is a difference between the expected result and the actual result.

Bug Report Components

1. Bug ID
2. Title
3. Description
4. Steps to Reproduce
5. Expected Result
6. Actual Result
7. Severity
8. Priority

Severity
- Technical impact

Priority
- Business urgency

Real QA Example

Bug ID

BUG101

Title

Login fails with valid credentials

Description

User cannot log in using valid email and password.

Steps

Open application.
Click Login.
Enter valid email.
Enter valid password.
Click Login.

Expected

User should successfully log in.

Actual

Error message: "Invalid Credentials."

Severity

High

Priority

High

Manual Testing Connection

As a Manual Tester, after executing a failed test case:

Reproduce the issue.
Collect evidence (screenshots/logs if available).
Create a bug report.
Assign it to the development team.
Automation Testing Connection

Automation tools can detect failures.

However, QA Engineers still analyze the failure and create bug reports.

Automation finds problems faster.

Humans explain them.

Beginner Mistakes
❌ Bad Title
Login issue

Good

Login fails with valid credentials
❌ Missing Steps

Developer cannot reproduce the bug.

Always provide clear steps.

❌ Wrong Severity

A spelling mistake is not Critical.

Login failure is not Low.

Choose severity carefully.

❌ Confusing Severity and Priority

Remember:

Severity

→ Technical impact.

Priority

→ Business urgency.

Memory Trick

Think of a hospital.

Severity

How badly is the patient injured?

Priority

Who should the doctor treat first?

Sometimes a less severe issue gets higher priority because of business needs, just like a patient who needs immediate attention.