# Test Case Design

**Application:** Online Appointment Booking System  
**Techniques:** Equivalence Partitioning, Boundary Value Analysis, Decision Table, State Transition Testing.

| ID | Technique | Preconditions / data | Steps | Expected result |
|---|---|---|---|---|
| TC01 | Equivalence partitioning (valid class) | Name, valid email, service, today/future date, time | Complete all fields and submit | Success message and confirmed appointment displayed |
| TC02 | Decision table / invalid class | Leave name blank; fill other required fields | Submit form | Browser blocks submission and no appointment is created |
| TC03 | Equivalence partitioning | Use malformed email such as `not-an-email` | Complete remaining fields and submit | Browser rejects invalid email; no appointment created |
| TC04 | BVA | Select yesterday | Attempt to submit a complete form | Past date cannot be selected or is rejected; no appointment created |
| TC05 | Decision table | Book a date/time, then submit same date/time again | Make two bookings for same slot | Second booking rejected with duplicate-slot message |
| TC06 | State transition | One confirmed appointment exists | Click its Cancel button | Status changes to Cancelled and success message appears |
| TC07 | Valid class | Use a different available time | Book an appointment | Booking succeeds |
| TC08 | State transition / regression | Cancel a booking, then book the same date/time again | Reuse the cancelled slot | Booking is accepted because cancelled bookings do not occupy the slot |

## Test data
Use fictional names and non-personal test emails, for example `test.user@example.com`. Do not enter real patient or sensitive information.

## Actual results
Record actual results in `03_Test_Execution/test_execution.md` after running the tests. Do not mark a case Pass without execution evidence.
