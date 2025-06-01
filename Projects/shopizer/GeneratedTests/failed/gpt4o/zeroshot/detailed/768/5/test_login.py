from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/")

        # Accept cookies
        try:
            cookie_accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_accept_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not found or clickable: {str(e)}")

        # Click account icon/button
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found or clickable: {str(e)}")

        # Click the "Login" link
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or clickable: {str(e)}")

        # Wait for login form
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username")))
        except Exception as e:
            self.fail(f"Login form elements not found: {str(e)}")

        # Fill in the login form
        driver.find_element(By.NAME, "username").send_keys("test2@user.com")
        driver.find_element(By.NAME, "loginPassword").send_keys("test**11")

        # Click the Login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']/..")))
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or clickable: {str(e)}")

        # Verify successful login by checking URL
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Failed to redirect to '/my-account': {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()