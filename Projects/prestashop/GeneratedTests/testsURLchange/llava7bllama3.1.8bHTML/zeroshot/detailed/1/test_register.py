import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestRegistration(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8080/en/')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="login-link"]')))

    def test_register_user(self):
        # Click the login link from the top navigation
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="login-link"]')))
        login_link.click()

        # On the login page, click on the register link (e.g. "No account? Create one here")
        register_link = self.driver.find_elements(By.XPATH, "//a[contains(.,'No account? Create one here')]")
        if len(register_link) > 0:
            register_link[0].click()
        else:
            self.fail("Register link not found")

        # Fill in the following fields using credentials
        gender_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'gender-1')))
        gender_field.click()

        first_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'firstname')))
        first_name_field.send_keys('Test')

        last_name_field = self.driver.find_elements(By.XPATH, "//input[@id='lastname']")
        if len(last_name_field) > 0:
            last_name_field[0].send_keys('User')
        else:
            self.fail("Last name field not found")

        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        email = f'test_{self.generate_random_string(6)}@user.com'
        email_field.send_keys(email)

        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys('test@user1')

        birthday_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'birthday')))
        birthday_field.send_keys('01/01/2000')

        # Tick checkboxes for privacy, newsletter, terms, etc.
        checkbox_privacy = self.driver.find_elements(By.XPATH, "//input[@data-name='privacy']")
        if len(checkbox_privacy) > 0:
            checkbox_privacy[0].click()
        else:
            self.fail("Privacy checkbox not found")

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-name="submit"]')))
        submit_button.click()

        # Wait for the redirect after login
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='sign-out']")))
        except TimeoutException as e:
            self.fail("No login page found")

        # Confirm that login was successful by checking that:
        # - The "Sign out" button is present in the top navigation
        sign_out_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='sign-out']")))
        self.assertEqual(sign_out_button.text.strip(), 'Sign out')

        # - The username (e.g. "test user") is also visible in the top navigation
        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='username']")))
        self.assertIsNotNone(username)

    def generate_random_string(self, length):
        import random
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()