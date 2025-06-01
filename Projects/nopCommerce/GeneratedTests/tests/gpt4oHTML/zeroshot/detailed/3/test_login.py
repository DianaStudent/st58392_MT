import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page.
        driver.get("http://example.com")  # Replace with actual home URL if needed.

        # Step 2: Click the "Login" button in the top navigation - assuming "My Account" leads to login.
        my_account_link = wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[@href='/customer/info']")))
        ActionChains(driver).move_to_element(my_account_link).click().perform()

        # Step 3: Wait until the login page loads fully.
        login_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1")))
        self.assertEqual(login_title.text, "Welcome, Please Sign In!")

        # Step 4: Fill in the email and password fields using the provided credentials.
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_input.send_keys("admin@admin.com")

        password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_input.send_keys("admin")

        # Step 5: Click the login button.
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.login-button")))
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Log out']")))
            self.assertIsNotNone(logout_button)
        except:
            self.fail("Log out button not found. Login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()