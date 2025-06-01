from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 1. Click on the account icon/button in the top-right.
        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 2. Wait for the dropdown and click the "Login" link.
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
        )
        login_link.click()

        # 3. Wait for the login form to appear.
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # 4. Fill in the username and password fields.
        username_field.send_keys("test2@user.com")
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        password_field.send_keys("test**11")

        # 5. Click the login button.
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
        )
        login_button.click()

        # 6. Wait for redirection or page update.
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))

        # 7. Confirm successful login by verifying the URL.
        current_url = driver.current_url
        if not current_url:
            self.fail("Current URL is empty after login.")
        if "/my-account" not in current_url:
            self.fail(f"Login failed. Expected URL to contain '/my-account', but got: {current_url}")

if __name__ == "__main__":
    unittest.main()