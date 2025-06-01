import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = self.wait.until(EC.presence_of_element_located(sign_in_link_locator))
        sign_in_link.click()

        # 3. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        self.wait.until(EC.presence_of_element_located(email_field_locator))

        # 4. Fill in the email and password fields using test credentials provided.
        email_field = self.driver.find_element(*email_field_locator)
        password_field_locator = (By.ID, "field-password")
        password_field = self.driver.find_element(*password_field_locator)

        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # 5. Click the submit button.
        submit_button_locator = (By.ID, "submit-login")
        submit_button = self.driver.find_element(*submit_button_locator)
        submit_button.click()

        # 6. Wait for the redirect after login.
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        self.wait.until(EC.presence_of_element_located(sign_out_link_locator))

        # 7. Confirm that login was successful.
        #   - The "Sign out" button is present in the top navigation
        #   - The username (e.g. "test user") is also visible in the top navigation.
        try:
            sign_out_link = self.driver.find_element(*sign_out_link_locator)
            sign_out_text = sign_out_link.text
            self.assertIn("Sign out", sign_out_text)
        except Exception as e:
            self.fail(f"Sign out link not found or text is incorrect: {e}")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
        try:
            username_element = self.driver.find_element(*username_locator)
            username_text = username_element.text
            self.assertTrue(username_text is not None and username_text != "", "Username is empty")
        except Exception as e:
            self.fail(f"Username element not found or text is empty: {e}")

if __name__ == "__main__":
    unittest.main()