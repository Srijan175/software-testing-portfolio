# Test Execution Summary

**Run date:** 19 November 2026
**Environment:** Ubuntu on WSL, Python 3.14.4, pytest 8.4.2, Selenium with Chrome
**Test command:** `pytest -v 05_Test_Automation/test_appointment_booking.py`

| Metric | Actual count |
|---|---:|
| Planned test cases | 8 |
| Automated tests executed | 4 |
| Passed | 4 |
| Failed | 0 |
| Not executed | 4 |

## Key findings

All four automated tests in the current suite passed:
- Valid appointment booking and confirmation
- Required name field validation
- Duplicate confirmed slot rejection
- Appointment cancellation and state change

The past-date test was removed from the automated suite and was not counted as passed. Invalid email validation, separate booking at another available time, and reuse of a cancelled slot were not independently tested in this run.

## Limitations

This educational application stores appointments in memory and does not test real authentication, notifications, databases, payments, or production security.

## Evidence

The latest terminal test output reported four passed tests and zero failed tests. Attach the actual terminal output or a generated test report as evidence.
