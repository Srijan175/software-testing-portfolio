# Test Execution Log

**Execution date/time:** 19 November 2026
**Executed by:** Student
**Environment:** Ubuntu on WSL, Python 3.14.4, pytest 8.4.2, Selenium with Chrome
**Command:** `pytest -v 05_Test_Automation/test_appointment_booking.py`

| Test ID | Actual result | Status (Pass/Fail/Not executed) | Evidence filename | Notes |
|---|---|---|---|---|
| TC01 | Success message and confirmed appointment displayed | Pass | TC01_valid_booking.png | Automated test passed |
| TC02 | Blank required name prevented booking | Pass | TC02_required_name.png | Automated test passed |
| TC03 | Invalid email validation | Not executed | N/A | Not included in current automated test run |
| TC04 | Past-date rejection | Not executed | N/A | Test removed from the automated suite |
| TC05 | Duplicate time slot rejected | Pass | TC05_duplicate_slot.png | Automated test passed |
| TC06 | Appointment status changed to Cancelled | Pass | TC06_cancel_appointment.png | Automated test passed |
| TC07 | Booking at a different available time | Not executed separately | N/A | No separate test in the current suite |
| TC08 | Rebooking a cancelled time slot | Not executed | N/A | Not included in the current automated test run |

**Execution summary:** Four automated tests passed and zero failed in the latest successful run. Four planned test cases were not independently executed.

**Note:** Verify that screenshot files exist before treating them as submission evidence.
