DAY 25 – JIRA

What is Jira?

Jira is a bug tracking and project management tool used to manage software projects and defects.

Main Uses

- Report bugs
- Assign bugs
- Track bug status
- Manage tasks

Common Bug Status

Open
In Progress
Ready for Testing
Closed
Reopened

Main Fields

- Summary
- Description
- Steps
- Expected Result
- Actual Result
- Priority
- Assignee


QA Workflow Example

Requirement:

Login should work.

You test it.

Bug found.

Create Jira ticket.

Developer fixes it.

Status changes:

Open

↓

In Progress

↓

Ready for Testing

You retest.

If fixed:

Closed

If still broken:

Reopened
Manual Testing Connection

Every bug you report is usually entered into Jira.

Manual testers spend a lot of time updating bug status and tracking defects.

Automation Testing Connection

Automation scripts can detect failures, but QA engineers still analyze them and create Jira tickets (or sometimes integrate automation tools with Jira).

Beginner Mistakes
❌ Writing vague summaries

Wrong:

Login issue

Correct:

Login fails with valid credentials
❌ Assigning wrong priority

Not every bug is High.

Choose priority based on business impact.

❌ Closing bugs without retesting

QA should verify the fix before marking a bug as closed.