import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click 'Sign in' from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='login']")))
        self.assertTrue(login_link, "Login link not found")
        login_link.click()

        # Step 2: Click 'Create one here'
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link, "Register link not found")
        register_link.click()

        # Step 3: Fill the registration form
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        self.assertTrue(gender_mr, "Gender selection not found")
        gender_mr.click()

        firstname = driver.find_element(By.ID, "field-firstname")
        self.assertTrue(firstname, "First name input not found")
        firstname.send_keys("Test")

        lastname = driver.find_element(By.ID, "field-lastname")
        self.assertTrue(lastname, "Last name input not found")
        lastname.send_keys("User")

        # Generate dynamic email
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        email_field = driver.find_element(By.ID, "field-email")
        self.assertTrue(email_field, "Email input not found")
        email_field.send_keys(email)

        password = driver.find_element(By.ID, "field-password")
        self.assertTrue(password, "Password input not found")
        password.send_keys("test@user1")

        birthday = driver.find_element(By.ID, "field-birthday")
        self.assertTrue(birthday, "Birthday input not found")
        birthday.send_keys("01/01/2000")

        # Step 4: Tick checkboxes
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        self.assertTrue(privacy_checkbox, "Customer privacy checkbox not found")
        privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        self.assertTrue(terms_checkbox, "Terms and conditions checkbox not found")
        terms_checkbox.click()

        # Optionally:
        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        if newsletter_checkbox and not newsletter_checkbox.is_selected():
            newsletter_checkbox.click()

        # Step 5: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertTrue(save_button, "Submit button not found")
        save_button.click()

        # Step 6: Confirm successful login
        sign_out = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertTrue(sign_out and sign_out.is_displayed(), "Sign out button not displayed, registration failed.")

        username_span = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info .account span.hidden-sm-down")))
        self.assertTrue(username_span and username_span.is_displayed() and "Test User" in username_span.text, 
                        "Username not displayed or incorrect, registration failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()