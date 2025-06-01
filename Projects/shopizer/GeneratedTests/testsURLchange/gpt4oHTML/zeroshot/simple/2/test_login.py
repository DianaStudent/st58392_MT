import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")  # Example URL

    def test_login(self):
        driver = self.driver

        try:
            # Wait for and click the account icon
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            # Wait for and click the "Login" link
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Wait for the login form and fill it with credentials
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            username_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")

            # Submit the login form
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            login_button.click()

            # Verify successful redirection to the account page
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()