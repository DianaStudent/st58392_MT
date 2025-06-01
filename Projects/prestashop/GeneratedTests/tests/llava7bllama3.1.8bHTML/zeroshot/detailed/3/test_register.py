import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/new-products")

    def tearDown(self):
        self.driver.quit()

    def test_register_user(self):
        # Click the login link from the top navigation
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
        ).click()

        # On the login page, click on the register link (e.g. "No account? Create one here")
        register_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='h6' and contains(text(), 'Create one here')]"))
        )
        register_link.click()

        # Fill in the registration form
        gender_input = self.driver.find_element(By.NAME, "gender")
        gender_input.send_keys(1)  # Mr.

        first_name_input = self.driver.find_element(By.NAME, "firstname")
        first_name_input.send_keys("Test")

        last_name_input = self.driver.find_element(By.NAME, "lastname")
        last_name_input.send_keys("User")

        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys(f"test_{self.generate_random_string(10)}@user.com")  # Generate dynamic email

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("test@user1")

        birthday_input = self.driver.find_element(By.NAME, "birthday")
        birthday_input.send_keys("01/01/2000")

        # Tick checkboxes for privacy, newsletter, terms
        privacy_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[@data-name='privacy']"))
        )
        self.assertTrue(privacy_checkbox.is_selected())
        privacy_checkbox.click()  # Toggle it off to simulate user interaction

        newsletter_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[@data-name='newsletter']"))
        )
        self.assertFalse(newsletter_checkbox.is_selected())
        newsletter_checkbox.click()

        terms_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[@data-name='terms']"))
        )
        self.assertTrue(terms_checkbox.is_selected())

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        # Wait for the redirect after login
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )

        # Confirm that login was successful
        sign_out_button = self.driver.find_element(By.XPATH, "//a[@class='h6' and contains(text(), 'Sign out')]")
        username_text = self.driver.find_element(By.XPATH, "//span[@data-name='username']").text

        self.assertEqual(sign_out_button.text, "Sign out")
        self.assertTrue(username_text.startswith("test"))

    def generate_random_string(self, length):
        import random
        import string
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

if __name__ == '__main__':
    unittest.main()