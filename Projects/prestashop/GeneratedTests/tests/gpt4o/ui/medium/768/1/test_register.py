import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/registration")

    def test_key_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check presence of key UI elements
        try:
            # Navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            
            # Form fields
            first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            last_name_input = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            
            # Buttons
            save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

            # Interact with elements: Enter text and click 'Save' button
            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")
            email_input.send_keys("john.doe@example.com")
            password_input.send_keys("StrongPassword123")
            save_button.click()

            # Check no visible errors
            notifications = driver.find_elements(By.ID, "notifications")
            if notifications:
                for notification in notifications:
                    if not notification.is_displayed():
                        self.fail("Error notification is visible on form submission.")

        except Exception as e:
            self.fail(f"UI component is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()