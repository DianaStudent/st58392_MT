import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage (Assuming this step is to verify homepage is opened)
        homepage_title = driver.title
        self.assertTrue("My Store" in homepage_title, "Homepage title is incorrect")

        # 2. Click the login link from the top navigation.
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(login_link.is_displayed(), "Login link not found")
        login_link.click()

        # 3. On the login page, click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link.is_displayed(), "Register link not found")
        register_link.click()

        # 4. Fill in the registration form
        # Dynamically generate email
        dynamic_email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

        # Fill in the form fields
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        self.assertTrue(gender_mr.is_displayed(), "Gender radio button not found")
        gender_mr.click()

        first_name = driver.find_element(By.ID, "field-firstname")
        last_name = driver.find_element(By.ID, "field-lastname")
        email = driver.find_element(By.ID, "field-email")
        password = driver.find_element(By.ID, "field-password")
        birthday = driver.find_element(By.ID, "field-birthday")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys(dynamic_email)
        password.send_keys("test@user1")
        birthday.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        privacy_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox = driver.find_element(By.NAME, "customer_privacy")

        self.assertTrue(privacy_checkbox.is_displayed(), "Privacy checkbox not found")
        self.assertTrue(terms_checkbox.is_displayed(), "Terms checkbox not found")

        privacy_checkbox.click()
        terms_checkbox.click()

        # 6. Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit")
        self.assertTrue(save_button.is_displayed(), "Save button not found")
        save_button.click()

        # 7. Wait for the redirect after login
        sign_out_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertTrue(sign_out_button.is_displayed(), "Sign out button not found after registration")

        # 8. Confirm login was successful by checking user information
        user_name_display = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Test User']")))
        self.assertTrue(user_name_display.is_displayed(), "User display name not visible after registration")

if __name__ == '__main__':
    unittest.main()