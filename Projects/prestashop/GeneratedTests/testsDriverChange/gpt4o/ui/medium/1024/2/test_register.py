import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
    
    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        
        try:
            # Check navigation links
            nav_links = [
                "Home", 
                "Clothes", 
                "Accessories", 
                "Art"
            ]
            for link_text in nav_links:
                link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
                self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")

            # Check form fields
            form_fields = [
                ("id_gender", (By.ID, "field-id_gender-1")),
                ("firstname", (By.ID, "field-firstname")),
                ("lastname", (By.ID, "field-lastname")),
                ("email", (By.ID, "field-email")),
                ("password", (By.ID, "field-password"))
            ]
            for name, (by, value) in form_fields:
                field = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((by, value))
                )
                self.assertTrue(field.is_displayed(), f"{name} field is not visible")

            # Check buttons
            buttons = [
                ("Save", (By.CSS_SELECTOR, "button[type='submit']")),
                ("Show", (By.CSS_SELECTOR, "button[data-action='show-password']"))
            ]
            for name, (by, value) in buttons:
                button = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((by, value))
                )
                self.assertTrue(button.is_displayed(), f"{name} button is not visible")

            # Interact with one element
            save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            save_button.click()

            # Check that the UI updates visually
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-footer"))
            )

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()