from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class RegistrationUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
    
    def test_ui_elements_presence_and_functionality(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check if the main UI components are present
        try:
            # Navigation Links
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Form Fields
            firstname_field = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            lastname_field = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            
            # Buttons
            submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and @data-link-action='save-customer']")))
            
            # Banners
            header_banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-banner")))
            
        except Exception as e:
            self.fail(f"Required UI element is missing: {str(e)}")

        # Interact with one element
        try:
            # Check and click the submit button
            submit_button.click()
            
            # Check UI updates or elements maintain stability (no specific feedback to wait for due to lack of entry requirement)
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Create an account')]")))

        except Exception as e:
            self.fail(f"Interactivity issue occurred: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()