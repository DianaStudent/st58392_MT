import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the homepage
        self.assertTrue(wait.until(EC.presence_of_element_located((By.ID, "index"))), "Homepage did not load.")

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info a[href*='login']")))
        login_link.click()

        # Step 3: On login page, click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill in the registration form
        gender_radio = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_radio.click()

        firstname_input = driver.find_element(By.ID, "field-firstname")
        firstname_input.send_keys("Test")

        lastname_input = driver.find_element(By.ID, "field-lastname")
        lastname_input.send_keys("User")

        email_input = driver.find_element(By.ID, "field-email")
        random_number = random.randint(100000, 999999)
        email_input.send_keys(f"test_{random_number}@user.com")

        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys(Keys.CONTROL + "a")
        birthday_input.send_keys("01/01/2000")

        # Tick checkboxes for privacy, newsletter, terms, etc.
        checkboxes = ["optin", "psgdpr", "newsletter", "customer_privacy"]
        for checkbox in checkboxes:
            checkbox_element = driver.find_element(By.NAME, checkbox)
            if not checkbox_element.is_selected():
                checkbox_element.click()

        # Step 5: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, ".form-footer .btn-primary")
        save_button.click()

        # Step 6: Confirm successful registration
        sign_out_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout")))
        self.assertTrue(sign_out_button.is_displayed(), "Sign out button not displayed.")

        username_display = driver.find_element(By.CSS_SELECTOR, "a.account span")
        self.assertTrue(username_display.is_displayed(), "User name is not displayed in the top navigation.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()