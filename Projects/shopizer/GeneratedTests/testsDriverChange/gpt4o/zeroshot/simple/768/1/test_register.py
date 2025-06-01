import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Cookie consent button missing.")

        # Go to register page
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            ActionChains(driver).move_to_element(account_button).perform()
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            register_link.click()
        except:
            self.fail("Register link missing in account dropdown.")

        # Fill registration form
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "email")))
            email_input.send_keys(f"test_{int(time.time())}@example.com")

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")

            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")

            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")

            country_select = driver.find_element(By.CSS_SELECTOR, "select:nth-of-type(1)")
            country_select.send_keys("Canada")

            state_select = driver.find_element(By.CSS_SELECTOR, "select:nth-of-type(2)")
            state_select.send_keys("Quebec")

            register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_button.click()
        except Exception as e:
            self.fail(f"Registration form error: {e}")

        # Check successful registration and redirection
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Redirection to /my-account page failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()