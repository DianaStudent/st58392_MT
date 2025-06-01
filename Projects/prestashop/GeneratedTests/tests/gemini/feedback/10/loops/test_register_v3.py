import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]")))
        register_link.click()

        # 4. Fill in the registration form.
        # Generate dynamic email
        email = "test_" + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + "@user.com"

        # Select Gender
        gender_radio_button = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_radio_button.click()

        # Fill First Name
        firstname_input = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        firstname_input.send_keys("Test")

        # Fill Last Name
        lastname_input = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        lastname_input.send_keys("User")

        # Fill Email
        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.send_keys(email)

        # Fill Password
        password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.send_keys("test@user1")

        # Fill Birthday
        birthday_input = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_input.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # Tick 'I agree to the terms and conditions and the privacy policy'
        psgdpr_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        psgdpr_checkbox.click()

        # Tick 'Customer data privacy'
        customer_privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//footer[@class='form-footer clearfix']/button[@type='submit']")))
        save_button.click()

        # 7. Wait for the redirect after registration.
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")))

        # 8. Confirm that registration was successful
        # Check "Sign out" button
        sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")))
        sign_out_text = sign_out_link.text
        self.assertIsNotNone(sign_out_text, "Sign out link text is empty")
        self.assertEqual(sign_out_text.strip(), "Sign out", "Sign out link not found")

        # Check username
        username_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span")))
        username_text = username_link.text
        self.assertIsNotNone(username_text, "Username text is empty")
        self.assertEqual(username_text.strip(), "Test User", "Username not found")

if __name__ == "__main__":
    unittest.main()