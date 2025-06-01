from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.email = "test@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # 1. Open the homepage.
        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(sign_in_link_locator)
        )
        sign_in_link.click()

        # 3. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(email_field_locator)
        )

        # 4. Fill in the email and password fields.
        email_field = driver.find_element(*email_field_locator)
        password_field_locator = (By.ID, "field-password")
        password_field = driver.find_element(*password_field_locator)

        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        # 5. Click the submit button.
        submit_button_locator = (By.ID, "submit-login")
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(submit_button_locator)
        )
        submit_button.click()

        # 6. Wait for the redirect after login.
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(sign_out_link_locator)
        )

        # 7. Confirm that login was successful.
        #   - The "Sign out" button is present in the top navigation
        #   - The username (e.g. "test user") is also visible in the top navigation.
        try:
            sign_out_link = driver.find_element(*sign_out_link_locator)
            self.assertIsNotNone(sign_out_link, "Sign out link is not present")
            self.assertEqual(sign_out_link.text, "Sign out", "Sign out link text is incorrect")
        except Exception as e:
            self.fail(f"Failed to find or assert Sign out link: {e}")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
        try:
            username_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(username_locator)
            )
            self.assertIsNotNone(username_element, "Username element is not present")
            self.assertTrue(len(username_element.text) > 0, "Username is empty")
        except Exception as e:
            self.fail(f"Failed to find or assert username: {e}")

if __name__ == "__main__":
    unittest.main()