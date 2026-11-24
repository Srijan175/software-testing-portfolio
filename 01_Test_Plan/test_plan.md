# Test Plan — Online Appointment Booking System

## 1. Objective
Verify that a user can submit a valid appointment, that invalid input is rejected, duplicate confirmed slots are prevented, and cancellation changes the appointment state.

## 2. Application under test
Local educational demo at `http://127.0.0.1:8000`. This is a sample app included with the portfolio, not a production healthcare service.

## 3. Scope
**In scope:** required fields, email input validation, date boundary, booking confirmation, duplicate-slot validation, cancellation.
**Out of scope:** authentication, database persistence, notifications, payment, load/security testing.

## 4. Test environment
- OS: Fill in after execution
- Python version: Fill in after execution (`python --version`)
- Browser: Google Chrome (record version if required)
- Libraries: Selenium WebDriver, pytest
- URL: `http://127.0.0.1:8000`

## 5. Test approach
1. Start the demo server.
2. Run automated tests with pytest.
3. Capture screenshots and JUnit XML report.
4. Review results and document any failures as potential defects.
5. Re-run tests after fixes.

## 6. Entry criteria
- Python and Chrome installed.
- Dependencies installed from `requirements.txt`.
- Demo server reachable at the test URL.

## 7. Exit criteria
- All planned test cases executed.
- Results and evidence recorded.
- Failures investigated and documented; no results fabricated.

## 8. Risks and limitations
The demo stores data in memory and is intended only for learning. It does not use real patient information. Browser-driver setup may require internet access on first run.
