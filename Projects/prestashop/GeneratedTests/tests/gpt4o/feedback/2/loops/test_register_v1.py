import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080/en/"
        self.email = f"test_{int(time.time())}@user.com"

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 2: Click the login link from the top navigation
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/en/login?back"]'))
        ).click()

        # Step 3: Click on the register link
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'No account? Create one here'))
        ).click()

        # Step 4: Fill in the following fields using credentials
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'field-id_gender-1'))
        ).click()

        driver.find_element(By.ID, 'field-firstname').send_keys('Test')
        driver.find_element(By.ID, 'field-lastname').send_keys('User')
        driver.find_element(By.ID, 'field-email').send_keys(self.email)
        driver.find_element(By.ID, 'field-password').send_keys('test@user1')
        driver.find_element(By.ID, 'field-birthday').send_keys('01/01/2000')

        # Step 5: Tick checkboxes for privacy, newsletter, terms, etc.
        checkboxes = ['optin', 'psgdpr', 'newsletter', 'customer_privacy']
        
        for checkbox in checkboxes:
            checkbox_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, checkbox))
            )
            
            if not checkbox_element.is_selected():
                checkbox_element.click()

        # Step 6: Submit the registration form.
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.assertIsNotNone(submit_button, "Submit button not found.")
        submit_button.click()

        # Step 7: Wait for the redirect after login.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.logout'))
        )

        # Step 8: Confirm the registration success.
        sign_out = driver.find_elements(By.CSS_SELECTOR, 'a.logout')
        user_name = driver.find_elements(By.CSS_SELECTOR, 'a.account span')
        
        self.assertTrue(len(sign_out) > 0 and len(user_name) > 0,
                        "Sign out button or user name not found, registration might not have been successful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()