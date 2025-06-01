import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Already done in setUp)

        # 2. Click the "My account" button in the top navigation.
        try:
            my_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link: {e}")

        # 3. Wait until the login page loads fully.
        try:
            login_page_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Welcome, Please Sign In!']")))
        except Exception as e:
            self.fail(f"Failed to load login page: {e}")

        # 4. Fill in the email and password fields using the provided credentials.
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))

            email_field.send_keys("admin@admin.com")
            password_field.send_keys("admin")

        except Exception as e:
            self.fail(f"Failed to fill email or password fields: {e}")

        # 5. Click the login button.
        try:
            login_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-button")))
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click login button: {e}")

        # 6. Verify that the user is logged in by checking the "Administration" button is present in the top navigation.
        try:
            admin_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Administration")))
            self.assertTrue(admin_link.is_displayed(), "Administration link is not displayed after login.")
        except Exception as e:
            self.fail(f"Failed to find 'Administration' link after login: {e}")

if __name__ == "__main__":
    unittest.main()