import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.email = "test@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_in_link_locator)
        )
        sign_in_link.click()

        # 2. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_field_locator)
        )

        # 3. Fill in the email and password fields.
        email_field = driver.find_element(*email_field_locator)
        password_field_locator = (By.ID, "field-password")
        password_field = driver.find_element(*password_field_locator)

        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        # 4. Click the submit button.
        submit_button_locator = (By.ID, "submit-login")
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        submit_button.click()

        # 5. Wait for the redirect after login.
        sign_out_link_locator = (By.XPATH, "//a[contains(@class, 'logout')]")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_out_link_locator)
        )

        # 6. Confirm that login was successful.
        # Check for "Sign out" button
        sign_out_link = driver.find_element(*sign_out_link_locator)
        if not sign_out_link:
            self.fail("Sign out link is not present after login.")
        sign_out_text = sign_out_link.text
        if not sign_out_text or "Sign out" not in sign_out_text:
            self.fail(f"Sign out link text is incorrect: {sign_out_text}")

        # Check for username
        username_locator = (By.XPATH, "//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
        try:
            username_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(username_locator)
            )
            username_text = username_element.text
            if not username_text:
                self.fail("Username is empty after login.")
        except:
            self.fail("Username element not found after login")

if __name__ == "__main__":
    unittest.main()