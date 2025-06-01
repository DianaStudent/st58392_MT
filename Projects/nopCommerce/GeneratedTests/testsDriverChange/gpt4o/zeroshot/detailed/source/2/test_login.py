import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        # Step 1: Verify navigation bar and click "My account"
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
        except:
            self.fail("Login button (My account) not found in the navigation bar.")

        my_account_link.click()

        # Step 2: Wait for login page to load
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
        except:
            self.fail("Login page did not load or email input field missing.")

        # Step 3: Fill in login form
        email_field.send_keys("admin@admin.com")
        driver.find_element(By.ID, "Password").send_keys("admin")

        # Step 4: Submit the form
        driver.find_element(By.CSS_SELECTOR, "button.login-button").click()

        # Step 5: Verify "Log out" is present
        try:
            log_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("Login was unsuccessful, 'Log out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()