import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.driver.maximize_window()

    def test_ui_elements_are_visible(self):
        driver = self.driver

        try:
            # Header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )

            # Main Form Elements
            form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "customer-form"))
            )

            # Form Fields
            firstname = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-firstname"))
            )

            lastname = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-lastname"))
            )

            email = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )

            password = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            birthday = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-birthday"))
            )

            # Checkboxes
            optin = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "optin"))
            )

            newsletter = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "newsletter"))
            )

            psgdpr = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "psgdpr"))
            )

            customer_privacy = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "customer_privacy"))
            )

            # Submit Button
            save_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((
                    By.XPATH, "//button[@data-link-action='save-customer']"))
            )

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()