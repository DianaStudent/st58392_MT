import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_elements_present_and_interactive(self):
        driver = self.driver

        # Check for the presence of key elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header, "Header is not visible")

            nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a")))
            self.assertGreater(len(nav_links), 0, "Navigation links are not visible")

            login_form = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-register-form form")))
            self.assertIsNotNone(login_form, "Login form is not visible")

            username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            self.assertIsNotNone(username_input, "Username input is not visible")
            self.assertIsNotNone(password_input, "Password input is not visible")

            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            self.assertIsNotNone(login_button, "Login button is not visible")

            # Interact with elements
            username_input.send_keys("test@example.com")
            password_input.send_keys("password")
            login_button.click()

            # Check that interaction causes expected changes
            WebDriverWait(driver, 5).until(EC.url_changes("http://localhost/login"))
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()