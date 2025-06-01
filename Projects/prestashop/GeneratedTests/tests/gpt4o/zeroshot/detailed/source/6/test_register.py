import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
    
    def test_user_registration(self):
        driver = self.driver

        # Step 1: Open the homepage and check if "Sign in" link exists
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']"))
            )
            sign_in_link.click()
        except:
            self.fail("Sign in link not found on homepage")

        # Step 2: On the login page, click on the register link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here"))
            )
            register_link.click()
        except:
            self.fail("Register link not found on login page")

        # Step 3: Fill in the registration form with credentials
        try:
            gender_mr = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-id_gender-1"))
            )
            gender_mr.click()

            first_name = driver.find_element(By.ID, "field-firstname")
            first_name.send_keys("Test")

            last_name = driver.find_element(By.ID, "field-lastname")
            last_name.send_keys("User")

            dynamic_email = f"test_{random.randint(100000, 999999)}@user.com"
            email_input = driver.find_element(By.ID, "field-email")
            email_input.send_keys(dynamic_email)

            password_input = driver.find_element(By.ID, "field-password")
            password_input.send_keys("test@user1")

            birthday_input = driver.find_element(By.ID, "field-birthday")
            birthday_input.send_keys("01/01/2000")

            privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
            privacy_checkbox.click()

            terms_checkbox = driver.find_element(By.NAME, "psgdpr")
            terms_checkbox.click()

            newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
            newsletter_checkbox.click()

            submit_button = driver.find_element(By.CLASS_NAME, "form-control-submit")
            submit_button.click()
        except:
            self.fail("Error filling the registration form")

        # Step 4: Confirm successful registration by checking "Sign out" and username
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            username_display = driver.find_element(By.XPATH, "//a[contains(@class, 'account')]/span")
            self.assertTrue("Test User" in username_display.text)
        except:
            self.fail("Registration failed: Sign out link or username not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()