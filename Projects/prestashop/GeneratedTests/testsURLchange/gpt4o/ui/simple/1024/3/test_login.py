import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        try:
            # Check header
            self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))

            # Check email input field
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))

            # Check password input field
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))

            # Check login button
            self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))

            # Check forgot password link
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))

            # Check registration link
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))

            # Check navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

        except Exception as e:
            self.fail(f"Test failed due to missing UI component: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()