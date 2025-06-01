from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
    
    def test_registration_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check if header is visible
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except Exception as e:
            self.fail(f"Header is not visible: {str(e)}")

        # Check if footer is visible
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except Exception as e:
            self.fail(f"Footer is not visible: {str(e)}")

        # Check if the navigation is visible
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-nav')))
        except Exception as e:
            self.fail(f"Navigation is not visible: {str(e)}")

        # Check form elements are present and visible
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'customer-form')))
            wait.until(EC.visibility_of_element_located((By.ID, 'field-firstname')))
            wait.until(EC.visibility_of_element_located((By.ID, 'field-lastname')))
            wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
            wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-link-action="save-customer"]')))
        except Exception as e:
            self.fail(f"Form elements are not visible: {str(e)}")

        # Interact with a button and check visual reaction
        try:
            save_button = driver.find_element(By.CSS_SELECTOR, 'button[data-link-action="save-customer"]')
            save_button.click()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'notifications-container')))
        except Exception as e:
            self.fail(f"UI did not react as expected after clicking: {str(e)}")

        # Check that all required elements exist and are visible
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-labelledby='language-selector-label']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Language dropdown']")))
        except Exception as e:
            self.fail(f"A required element is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()