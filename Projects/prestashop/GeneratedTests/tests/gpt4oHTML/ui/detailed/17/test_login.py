import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_ui_process(self):
        driver = self.driver

        # Step 1: Check visibility of structural elements
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))
        except Exception as e:
            self.fail(f"Structural elements are not visible: {str(e)}")

        # Step 2: Check presence and visibility of input fields, buttons, labels, sections
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-email")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-password")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "submit-login")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "login-form")))
        except Exception as e:
            self.fail(f"Input fields, buttons, labels, or sections are missing: {str(e)}")

        # Step 3: Interact with key UI elements
        try:
            email_input = driver.find_element(By.ID, "field-email")
            password_input = driver.find_element(By.ID, "field-password")
            sign_in_button = driver.find_element(By.ID, "submit-login")
            
            email_input.send_keys("test@example.com")
            password_input.send_keys("password")
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to interact with UI elements: {str(e)}")

        # Step 4: Confirm UI reactions (this could be customized based on application behavior after login)
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "account")))
        except Exception as e:
            self.fail(f"UI did not react as expected: {str(e)}")

        # Step 5: Asserting presence of all required UI elements
        required_ids = ["header", "footer", "field-email", "field-password", "submit-login", "login-form"]
        for element_id in required_ids:
            try:
                element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, element_id)))
                self.assertTrue(element.is_displayed(), f"Required element with ID '{element_id}' is not visible.")
            except Exception as e:
                self.fail(f"Required element '{element_id}' is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()