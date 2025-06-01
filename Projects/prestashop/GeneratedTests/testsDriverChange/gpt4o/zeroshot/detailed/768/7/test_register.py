import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import string
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def generate_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
    
    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage
        driver.get("http://localhost:8080/en/")
        
        # 2. Click the login link from the top navigation.
        login_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, '/en/login')]"))
        )
        login_link.click()
        
        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        register_link.click()

        # 4. Fill in the form fields
        email_address = self.generate_email()

        gender_radio = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='field-id_gender-1']"))
        )
        gender_radio.click()

        firstname_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        firstname_field.send_keys("Test")

        lastname_field = driver.find_element(By.ID, "field-lastname")
        lastname_field.send_keys("User")

        email_field = driver.find_element(By.ID, "field-email")
        email_field.send_keys(email_address)

        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys("test@user1")

        birthday_field = driver.find_element(By.ID, "field-birthday")
        birthday_field.send_keys("01/01/2000")

        # 5. Tick checkboxes
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()

        # 6. Submit the registration form.
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save']")
        submit_button.click()

        # 7. Wait for the redirect after login.
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/?mylogout=')]"))
        )

        # 8. Confirm successful login
        signout_link = driver.find_elements(By.XPATH, "//a[contains(@href, '/?mylogout=')]")
        self.assertTrue(signout_link, "Sign out button is not present - Login failed.")

        user_info = driver.find_elements(By.XPATH, "//div[@id='_desktop_user_info']//span[contains(text(), 'Test User')]")
        self.assertTrue(user_info, "User name is not displayed in the top navigation.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()