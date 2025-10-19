from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup WebDriver ---
driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.maximize_window()

# --- Open the website ---
driver.get("https://example.com")  # replace with your site URL

# --- Log in first (if needed) ---
username_input = driver.find_element(By.ID, "username")  # adjust selector
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-btn")

username_input.send_keys("your_username")
password_input.send_keys("your_password")
login_button.click()

# --- Wait until login completes ---
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "logout-btn"))  # adjust selector
)

# --- Log out ---
logout_button = driver.find_element(By.ID, "logout-btn")  # adjust selector
logout_button.click()

# --- Optional: Wait to confirm logout ---
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-btn"))  # user sees login page again
)

print("Logged out successfully!")

# --- Close browser ---
driver.quit()
