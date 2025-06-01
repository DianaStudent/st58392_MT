import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver

        # Wait until the registration page is loaded and elements are visible
        try:
            # Header: Register
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='page-title']//h1[text()='Register']"))
            )
            # Gender radio buttons
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "gender-male"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "gender-female"))
            )
            # First Name field
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "FirstName"))
            )
            # Last Name field
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "LastName"))
            )
            # Email field
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            # Password field
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Password"))
            )
            # Confirm Password field
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "ConfirmPassword"))
            )
            # Newsletter Checkbox
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Newsletter"))
            )
            # Register button
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "register-button"))
            )

        except Exception as e:
            self.fail(f"Element not found or visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()