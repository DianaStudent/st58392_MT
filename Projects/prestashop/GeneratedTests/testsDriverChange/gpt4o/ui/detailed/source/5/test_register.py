import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/registration")

    def test_UI_elements(self):
        # Verify structural elements
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header"))), "Header is missing.")
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer"))), "Footer is missing.")
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "nav"))), "Navigation is missing.")

        # Verify form elements
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname"))), "First name field is missing.")
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname"))), "Last name field is missing.")
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.ID, "field-email"))), "Email field is missing.")
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.ID, "field-password"))), "Password field is missing.")
        self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))), "Submit button is missing.")

        # Check label text
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "label[for='field-firstname']").text, "First name")
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "label[for='field-lastname']").text, "Last name")
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "label[for='field-email']").text, "Email")
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "label[for='field-password']").text, "Password")

        # Interact with UI elements
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Confirm that clicking the submit button does not remove key elements
        self.assertTrue(self.driver.find_element(By.ID, "field-firstname").is_displayed(), "First name field is not visible after clicking submit.")
        self.assertTrue(self.driver.find_element(By.ID, "field-lastname").is_displayed(), "Last name field is not visible after clicking submit.")

    def tearDown(self):
        # Close browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()