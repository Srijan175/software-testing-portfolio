# Selenium automation

The tests use Python, Selenium WebDriver and pytest against the local demo app.

From the repository root:
1. Start the app with `python run_app.py`.
2. In another terminal, activate the virtual environment and run `pytest -v`.
3. For an XML report, run `pytest -v --junitxml=test-results/junit.xml`.
4. Screenshots from tests are saved to `05_Test_Automation/screenshots/`.

If Chrome does not start, install/update Google Chrome and update Selenium with `pip install -U selenium`. Selenium Manager attempts to handle the browser driver automatically. Keep the demo server running during tests.
