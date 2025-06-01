import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.email = "test2@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # 1. Click on the account icon/button in the top-right.
        account_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )

        # Use javascript to click the element
        driver.execute_script("arguments[0].click();", account_button)

        # 2. Wait for the dropdown and click the "Login" link.
        login_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='account-dropdown']//a[@href='/login']"))
        )
        login_link.click()

        # 3. Wait for the login form to appear.
        username_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )

        # 4. Fill in the username and password fields.
        username_field.send_keys(self.email)
        password_field.send_keys(self.password)

        # 5. Click the login button.
        login_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Login')]"))
        )
        login_button.click()

        # 6. Wait for redirection or page update.
        wait.until(EC.url_contains("/my-account"))

        # 7. Confirm successful login by verifying the URL.
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login failed. URL does not contain '/my-account'.")

if __name__ == "__main__":
    unittest.main()