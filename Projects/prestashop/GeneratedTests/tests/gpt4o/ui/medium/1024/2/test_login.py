import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_key_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check for header presence
            header = wait.until(EC.visibility_of_element_located((By.XPATH, "//header[@id='header']")))
            self.assertIsNotNone(header)

            # Check for navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            self.assertIsNotNone(home_link)

            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            self.assertIsNotNone(clothes_link)

            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            self.assertIsNotNone(accessories_link)

            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            self.assertIsNotNone(art_link)

            # Check for form fields
            email_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='field-email']")))
            self.assertIsNotNone(email_field)

            password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='field-password']")))
            self.assertIsNotNone(password_field)

            # Check for buttons
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submit-login']")))
            self.assertIsNotNone(login_button)

            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
            self.assertIsNotNone(register_link)

            # Interact with a button
            login_button.click()

            # Verify no errors appear (you might need to tailor this to your page specifics)
            error_notifications = driver.find_elements(By.XPATH, "//div[contains(@class, 'alert-danger')]")
            self.assertEqual(len(error_notifications), 0, "Errors found in UI after login attempt.")

        except Exception as e:
            self.fail(f"Test failed due to missing or non-visible element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()