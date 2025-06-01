import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        cookies_button_locator = (By.ID, "rcc-confirm-button")
        cookies_button = wait.until(EC.element_to_be_clickable(cookies_button_locator))
        cookies_button.click()

        # Step 2: Click on the account icon/button
        account_icon_locator = (By.CSS_SELECTOR, "button.account-setting-active")
        account_icon = wait.until(EC.element_to_be_clickable(account_icon_locator))
        account_icon.click()

        # Step 3: Click the "Login" link
        login_link_locator = (By.LINK_TEXT, "Login")
        login_link = wait.until(EC.element_to_be_clickable(login_link_locator))
        login_link.click()

        # Step 4: Wait for the login form to appear
        username_locator = (By.NAME, "username")
        wait.until(EC.presence_of_element_located(username_locator))

        # Step 5: Fill in the username and password fields using credentials
        email = "test2@user.com"
        password = "test**11"

        username_input = driver.find_element(*username_locator)
        password_locator = (By.NAME, "loginPassword")
        password_input = driver.find_element(*password_locator)

        username_input.send_keys(email)
        password_input.send_keys(password)

        # Step 6: Click the login button
        login_button_locator = (By.XPATH, "//button[span[text()='Login']]")
        login_button = wait.until(EC.element_to_be_clickable(login_button_locator))
        login_button.click()

        # Step 7: Wait and confirm successful login
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url, "Login was not successful, '/my-account' not in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()