# week 04
# Day 31 -  selenium Waits

1.What is waits?
    A waits tells selenium to pause untill an element is avaible before counting to next action.

without waits:
    Open page -> Immediatly search -> fail
with waits:
    open page -> wait -> element appear -> continue

2.Types of Waits:
    (1)Implicit wait
    (2)Explicit Wait

(1)Implicit wait:
    "whenever you cant find an element , wait up 10 secs, before giving up.
        -you say this to selenium. You write it once but it works everywhere, it waits upto the seconds we mention in scripts , once the task is it continue, within 10 secs , or before 10 secs.
(2)Explicit Waits:
    This waits only for specific element. Imagine login page , only login buttons loads slowly, so we have to wait for that specific one rather than others, here we use explicit waits.


3.Difference betweeen Implicit and Explicit:

Implicit Waits -> Global, One line for whole propject, Easy and less control.
Explicit waits -> Specific, One element at a time, More powerful and more control.


-- refer the practice file (day-31_waits.py) for example program and for better understanding--


