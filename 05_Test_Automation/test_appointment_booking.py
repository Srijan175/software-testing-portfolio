from datetime import date, timedelta
from pathlib import Path
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.getenv("APPOINTMENT_BASE_URL", "http://127.0.0.1:8000")
SCREENSHOT_DIR = Path(__file__).resolve().parent / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Uncomment the next line to run headless (without a visible browser window):
    # options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1280, 900)
    browser.get(BASE_URL)
    yield browser
    browser.quit()


def fill_form(driver, *, name="Test User", email="test.user@example.com",
              service="General Consultation", appointment_date=None, time="09:00"):
    if appointment_date is None:
        appointment_date = date.today().isoformat()
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    Select(driver.find_element(By.ID, "service")).select_by_visible_text(service)
    driver.find_element(By.ID, "date").send_keys(appointment_date)
    Select(driver.find_element(By.ID, "time")).select_by_visible_text(time)


def message_text(driver):
    return driver.find_element(By.ID, "message").text


def save_screenshot(driver, name):
    path = SCREENSHOT_DIR / name
    driver.save_screenshot(str(path))
    return path


def test_valid_booking_shows_confirmation(driver):
    fill_form(driver, time="09:00")
    driver.find_element(By.ID, "book-button").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "message"), "booked successfully")
    )
    assert "booked successfully" in message_text(driver)
    assert "Test User" in driver.find_element(By.ID, "appointments").text
    save_screenshot(driver, "TC01_valid_booking.png")


def test_required_name_field_is_validated(driver):
    fill_form(driver, name="")
    driver.find_element(By.ID, "book-button").click()
    name_field = driver.find_element(By.ID, "name")
    assert name_field.get_attribute("required") is not None
    assert len(driver.find_elements(By.CSS_SELECTOR, ".appointment")) == 0
    save_screenshot(driver, "TC02_required_name.png")


def test_duplicate_confirmed_slot_is_rejected(driver):
    fill_form(driver, time="10:00")
    driver.find_element(By.ID, "book-button").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "message"), "booked successfully")
    )
    fill_form(driver, time="10:00")
    driver.find_element(By.ID, "book-button").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "message"), "already booked")
    )
    assert "already booked" in message_text(driver)
    assert len(driver.find_elements(By.CSS_SELECTOR, ".appointment")) == 1
    save_screenshot(driver, "TC05_duplicate_slot.png")


def test_cancelled_appointment_changes_state(driver):
    fill_form(driver, time="11:00")
    driver.find_element(By.ID, "book-button").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "message"), "booked successfully")
    )
    card = driver.find_element(By.CSS_SELECTOR, ".appointment")
    card.find_element(By.CSS_SELECTOR, "button.cancel").click()
    assert "Cancelled" in driver.find_element(By.ID, "appointments").text
    assert "Appointment cancelled." in message_text(driver)
    save_screenshot(driver, "TC06_cancel_appointment.png")



