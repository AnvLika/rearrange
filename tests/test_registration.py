from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
from uuid import uuid4
import secrets
import string


fake = Faker()

def generate_user():
    """Return a dict with realistic, unique test credentials."""
    first_name = fake.first_name()
    last_name = fake.last_name()

    # make username safe and reasonably unique
    # e.g., student_jones_20251020_4f3a
    unique_suffix = uuid4().hex[:2]
    username = f"{first_name.lower()}_{last_name.lower()}_{unique_suffix}"

    # email: use faker OR construct unique email on a safe domain
    email = f"{username}@example.com"  # example.com is safe for tests
    # or: email = fake.unique.email()

    # password: create a secure-looking password meeting common rules
    def gen_password(length=12):
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_"
        # use secrets.choice for cryptographic randomness
        return ''.join(secrets.choice(alphabet) for _ in range(length))

<<<<<<< HEAD
    password = gen_password(7)
=======
    password = gen_password(14)
>>>>>>> aa39e45199c9d748024350a9bd8c1a678db6522b

    return {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password
    }

def test_log_in():
    assert True  # placeholder


    creds = generate_user()
    print("Generated:", creds)


    # --- Setup WebDriver ---
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.maximize_window()

    # --- Open the website ---
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")

    # --- Log in first (if needed) ---
    username_name = driver.find_element(By.ID, "firstName")
    username_last_name = driver.find_element(By.ID, "lastName")
    email_input = driver.find_element(By.ID,"email")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "submit")

    username_name.send_keys (creds["username"])
    username_last_name.send_keys(creds["last_name"])
    email_input.send_keys(creds["email"])
    password_input.send_keys(creds["password"])

    submit_button.click()


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logout"))  # user sees Log out btn
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Contact List']"))  # user sees header
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Contact List']"))  # user sees Contact List table
    )


<<<<<<< HEAD
    print("Registration was sucessfull!")
=======
    print("Registration was successfull!")
>>>>>>> aa39e45199c9d748024350a9bd8c1a678db6522b

    # --- Close browser ---
    driver.quit()
