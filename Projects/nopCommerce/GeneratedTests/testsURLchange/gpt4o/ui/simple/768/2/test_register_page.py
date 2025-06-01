import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        try:
            # Check header links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

            # Check form fields
            self.wait.until(EC.visibility_of_element_located((By.ID, "gender-male")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "gender-female")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Company")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Newsletter")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))

            # Check Register button
            self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

            # Check links in footer
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sitemap")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shipping & returns")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Privacy notice")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Conditions of Use")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()