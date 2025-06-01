import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://max/login?returnUrl=%2F')

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check key header links
            header_links = [
                "//a[contains(text(),'Register')]",
                "//a[contains(text(),'Log in')]",
                "//a[contains(text(),'Wishlist')]",
                "//a[contains(text(),'Shopping cart')]",
                "//a[contains(text(),'My account')]",
                "//a[contains(text(),'Blog')]",
                "//a[contains(text(),'Contact us')]"
            ]
            for link in header_links:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, link)))
                self.assertTrue(element.is_displayed(), f"{link} is not visible")

            # Check form elements
            email_input = wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")

            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'login-button')]")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'register-button')]")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")

            # Interact with elements
            login_button.click()

            # Verify no errors
            login_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'page-title')]/h1")))
            self.assertIn("Welcome, Please Sign In!", login_message.text, "Login page did not display correctly")

        except Exception as e:
            self.fail(f"An expected UI element is missing or an error occurred: {str(e)}")

if __name__ == "__main__":
    unittest.main()