import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Check Cookie Consent button
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Cookie Button not visible")

            # Check Header elements
            logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='logo']/a/img")))
            self.assertTrue(logo.is_displayed(), "Logo not visible")

            # Check Menu items
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            self.assertTrue(home_link.is_displayed(), "Home link not visible")
            self.assertTrue(tables_link.is_displayed(), "Tables link not visible")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link not visible")

            # Check Login form fields and buttons
            username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

            self.assertTrue(username_field.is_displayed(), "Username field not visible")
            self.assertTrue(password_field.is_displayed(), "Password field not visible")
            self.assertTrue(login_button.is_displayed(), "Login button not visible")

            # Check Forgot Password link
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot Password?")))
            self.assertTrue(forgot_password_link.is_displayed(), "Forgot Password link not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()