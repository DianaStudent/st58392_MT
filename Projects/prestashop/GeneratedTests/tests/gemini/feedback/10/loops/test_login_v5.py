import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    URL = "http://localhost:8080/en/"
    EMAIL = "test@user.com"
    PASSWORD = "test@user1"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the homepage.
        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        try:
            sign_in_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located(sign_in_link_locator))
            sign_in_link = driver.find_element(*sign_in_link_locator)
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(email_field_locator))
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # 4. Fill in the email and password fields.
        try:
            email_field = driver.find_element(*email_field_locator)
            password_field = driver.find_element(By.ID, "field-password")
            email_field.send_keys(self.EMAIL)
            password_field.send_keys(self.PASSWORD)
        except Exception as e:
            self.fail(f"Could not fill in email and password: {e}")

        # 5. Click the submit button.
        submit_button_locator = (By.ID, "submit-login")
        try:
            submit_button = driver.find_element(*submit_button_locator)
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not submit the login form: {e}")

        # 6. Wait for the redirect after login.
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(sign_out_link_locator))
        except Exception as e:
            self.fail(f"Login redirect did not occur: {e}")

        # 7. Confirm that login was successful.
        #   - The "Sign out" button is present in the top navigation
        #   - The username (e.g. "test user") is also visible in the top navigation.
        try:
            sign_out_link = driver.find_element(*sign_out_link_locator)
            self.assertIsNotNone(sign_out_link)
            self.assertEqual("Sign out", sign_out_link.text)

            username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
            username_element = driver.find_element(*username_locator)
            self.assertIsNotNone(username_element)
            self.assertTrue(len(username_element.text) > 0)

        except Exception as e:
            self.fail(f"Login verification failed: {e}")

if __name__ == "__main__":
    unittest.main()