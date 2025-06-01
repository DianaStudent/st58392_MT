import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_logo img")))
        self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")

        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu .category a")
        expected_links = ["http://localhost:8080/en/3-clothes", 
                          "http://localhost:8080/en/6-accessories", 
                          "http://localhost:8080/en/9-art"]
        self.assertEqual(len(nav_links), 3, "Not all navigation links are present")

        # Check form input fields
        first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        last_name_field = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        for element in [first_name_field, last_name_field, email_field]:
            self.assertTrue(element.is_displayed(), f"{element.get_attribute('name')} input is not visible")

        # Check buttons
        save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-footer button[type='submit']")))
        self.assertTrue(save_button.is_displayed(), "Save button is not visible")

        # Interact with form elements
        first_name_field.send_keys("John")
        last_name_field.send_keys("Doe")
        email_field.send_keys("john.doe@example.com")
        
        # Click the save button
        save_button.click()

        # Check for potential errors
        # For simplicity, we just ensure the page does not throw an error
        error_elements = driver.find_elements(By.CSS_SELECTOR, ".error")
        self.assertEqual(len(error_elements), 0, "Errors found in the UI")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()