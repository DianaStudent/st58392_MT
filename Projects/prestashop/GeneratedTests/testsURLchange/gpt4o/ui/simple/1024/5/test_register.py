import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        
    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check header links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Cart']")))

            # Check main menu items
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check form fields
            wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-1")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-2")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))
            
            # Check required checkboxes
            wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
            wait.until(EC.visibility_of_element_located((By.NAME, "customer_privacy")))

            # Check Save button
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and text()='Save']")))
        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()