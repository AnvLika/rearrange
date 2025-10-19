import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ------------------------
# Fixture: setup and teardown WebDriver
# ------------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------------
# Fixture: setup and teardown WebDriver
# ------------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

# ------------------------
# Test 1: Invalid username
# ------------------------
def test_log_in_invalid_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter credentials (invalid username)
    driver.find_element(By.ID, "username").send_keys("teacher")  # invalid
    driver.find_element(By.ID, "password").send_keys("Password123")  # valid password
    driver.find_element(By.ID, "submit").click()

    # Wait for error message
    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )

    # Assert error message
    assert "Your username is invalid!" in error_msg.text
    print("Invalid username test passed:", error_msg.text)

# ------------------------
# Test 2: Invalid password
# ------------------------
def test_log_in_invalid_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter credentials (valid username, invalid password)
    driver.find_element(By.ID, "username").send_keys("student")  # valid username
    driver.find_element(By.ID, "password").send_keys("Password124")  # invalid password
    driver.find_element(By.ID, "submit").click()

    # Wait for error message
    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )

    # Assert error message
    assert "Your password is invalid!" in error_msg.text
    print("Invalid password test passed:", error_msg.text)
