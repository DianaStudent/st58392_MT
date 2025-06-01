import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]")))
        register_link.click()

        # 4. Fill in the registration form.
        gender = "1"
        firstname = "Test"
        lastname = "User"
        email = f"test_{random.randint(100000, 999999)}@user.com"
        password = "test@user1"
        birthday = "01/01/2000"

        # Select gender
        gender_radio_locator = (By.XPATH, f"//input[@name='id_gender' and @value='{gender}']")
        gender_radio = wait.until(EC.presence_of_element_located(gender_radio_locator))
        gender_radio.click()

        # Fill in first name
        firstname_field = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        firstname_field.send_keys(firstname)

        # Fill in last name
        lastname_field = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        lastname_field.send_keys(lastname)

        # Fill in email
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_field.send_keys(email)

        # Fill in password
        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_field.send_keys(password)

        # Fill in birthday
        birthday_field = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_field.send_keys(birthday)

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        psgdpr_checkbox.click()

        newsletter_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))

        customer_privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]")))
        save_button.click()

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful.
        # Check for "Sign out" link
        sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]")))
        self.assertTrue("Sign out" in sign_out_link.text, "Sign out link not found after registration.")

        # Check for username
        username_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")))
        self.assertTrue(firstname in username_link.text, "Username not found after registration.")

if __name__ == "__main__":
    unittest.main()