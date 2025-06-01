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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # 1. Open the homepage.
        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_in_link_locator)
        )
        sign_in_link.click()

        # 3. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_field_locator)
        )

        # 4. Fill in the email and password fields.
        email_field = driver.find_element(*email_field_locator)
        password_field = driver.find_element(By.ID, "field-password")
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # 5. Click the submit button.
        submit_button_locator = (By.ID, "submit-login")
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        submit_button.click()

        # 6. Wait for the redirect after login.
        sign_out_link_locator = (By.XPATH, "//a[contains(@class, 'logout')]")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_out_link_locator)
        )

        # 7. Confirm that login was successful.
        #   - The "Sign out" button is present.
        #   - The username is also visible.
        try:
            sign_out_link = driver.find_element(*sign_out_link_locator)
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed")
            self.assertEqual(sign_out_link.text.strip(), "Sign out", "Sign out link text is incorrect")

            username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
            username_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(username_locator)
            )

            self.assertTrue(username_element.is_displayed(), "Username is not displayed")
            self.assertEqual(username_element.text.strip(), "test user", "Username is incorrect")

        except Exception as e:
            self.fail(f"Login verification failed: {e}")

if __name__ == "__main__":
    unittest.main()