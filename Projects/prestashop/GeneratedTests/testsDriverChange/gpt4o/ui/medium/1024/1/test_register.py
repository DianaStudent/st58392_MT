import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence(self):
        driver = self.driver
        
        # Verify navigation links
        self.assertTrue(self.is_element_present(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"))
        self.assertTrue(self.is_element_present(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"))
        self.assertTrue(self.is_element_present(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        
        # Verify form inputs
        self.assertTrue(self.is_element_present(By.ID, "field-firstname"))
        self.assertTrue(self.is_element_present(By.ID, "field-lastname"))
        self.assertTrue(self.is_element_present(By.ID, "field-email"))
        self.assertTrue(self.is_element_present(By.ID, "field-password"))
        
        # Verify buttons
        self.assertTrue(self.is_element_present(By.XPATH, "//button[@data-link-action='save-customer']"))
        
        # Verify language dropdown
        self.assertTrue(self.is_element_present(By.XPATH, "//button[@aria-label='Language dropdown']"))
        
        # Interact with an element
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-link-action='save-customer']")))
        save_button.click()

        # Check UI update (for demonstration, checking if a header is still present or error displayed)
        header_present = self.is_element_present(By.XPATH, "//h1[text()='Create an account']")
        self.assertTrue(header_present, "Header is not present, unexpected UI change after clicking save.")

    def is_element_present(self, how, what):
        try:
            self.wait.until(EC.visibility_of_element_located((how, what)))
            return True
        except:
            return False

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()