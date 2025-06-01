import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements_presence(self):
        driver = self.driver

        try:
            # Check presence and visibility of key elements
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-firstname"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-lastname"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-birthday"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@data-link-action='save-customer']"))
            )

            # Check navigation links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Cart"))
            )

            # Interact with a button and check UI update
            driver.find_element(By.XPATH, "//button[@data-link-action='save-customer']").click()

            # Check for potential UI errors here (log messages, alerts, etc.)
            # Add specific conditions to verify that no errors occur if applicable
            
        except Exception as e:
            self.fail(f"UI elements test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()