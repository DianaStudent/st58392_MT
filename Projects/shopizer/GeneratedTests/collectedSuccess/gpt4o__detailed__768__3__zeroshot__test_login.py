from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page (Already done in setUp)

        # Step 2: Click on the account icon/button in the top-right
        account_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        # Step 3: Wait for the dropdown and click the "Login" link
        login_link = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/login']")))
        login_link.click()

        # Step 4: Wait for the login form to appear
        username_input = wait.until(EC.element_to_be_clickable(
            (By.NAME, "username")))

        # Step 5: Fill in the username and password fields using credentials
        username_input.send_keys("test2@user.com")
        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys("test**11")

        # Step 6: Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Step 7: Wait for redirection or page update
        wait.until(EC.url_contains("/my-account"))

        # Step 8: Confirm successful login by checking the presence of account page
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login failed: User is not redirected to the account page.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()