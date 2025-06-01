import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = "test@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the login link in the top menu.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign in')]")
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(sign_in_link_locator)
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click Sign in link: {e}")

        # 3. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(email_field_locator)
            )
        except Exception as e:
            self.fail(f"Email field did not load: {e}")

        # 4. Fill in the email and password fields.
        email_field = driver.find_element(*email_field_locator)
        password_field = driver.find_element(By.ID, "field-password")

        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        # 5. Submit the login form.
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # 6. Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign out')]")
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_out_link_locator)
            )
            self.assertTrue("Sign out" in sign_out_link.text, "Sign out link not found after login")
        except Exception as e:
            self.fail(f"Sign out link not found or text incorrect: {e}")

if __name__ == "__main__":
    unittest.main()