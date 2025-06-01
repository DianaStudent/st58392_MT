import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        try:
            # Verify the presence and visibility of header links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-label")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-label")))

            # Verify the presence and visibility of search box
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))

            # Verify the presence and visibility of registration form elements
            self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))

            # Verify the presence and visibility of register button
            self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

        except Exception as e:
            self.fail(f"UI element test failed: {e}")

if __name__ == "__main__":
    unittest.main()