def test_log_in():
    assert True  # placeholder
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
    driver.get("https://practicetestautomation.com/practice-test-login/")  # replace with your site URL

    # --- Log in first (if needed) ---
    username_input = driver.find_element(By.ID, "username")  # adjust selector
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit")

    username_input.send_keys("student")
    password_input.send_keys("Password123")
    login_button.click()
    #
    # # --- Wait until login completes ---
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "logout-btn"))  # adjust selector
    # )
    #
    # # --- Log out ---
    # logout_button = driver.find_element(By.ID, "logout-btn")  # adjust selector
    # logout_button.click()
    #
    # --- Optional: Wait to confirm login ---
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Log out']"))  # user sees Log out btn
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("practicetestautomation.com/logged-in-successfully/")
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p/strong[contains(text(), 'Congratulations student. You successfully logged in!')]")),  # user sees congratulate message
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Logged In Successfully')]"))  # user sees he is Successfully logged in
    )

    print("Login successfully!")

    # --- Close browser ---
    driver.quit()
