import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
            
            # Form
            form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "customer-form"))
            )
            
            # Social title
            social_title = driver.find_element(By.XPATH, "//input[@name='id_gender']")
            self.assertTrue(social_title.is_displayed())

            # First name
            firstname = driver.find_element(By.ID, "field-firstname")
            self.assertTrue(firstname.is_displayed())

            # Last name
            lastname = driver.find_element(By.ID, "field-lastname")
            self.assertTrue(lastname.is_displayed())

            # Email
            email = driver.find_element(By.ID, "field-email")
            self.assertTrue(email.is_displayed())

            # Password
            password = driver.find_element(By.ID, "field-password")
            self.assertTrue(password.is_displayed())

            # Terms and Conditions checkbox
            terms_checkbox = driver.find_element(By.NAME, "psgdpr")
            self.assertTrue(terms_checkbox.is_displayed())

            # Submit button
            submit_button = driver.find_element(By.XPATH, "//button[@data-link-action='save-customer']")
            self.assertTrue(submit_button.is_displayed())

            # Additional Links
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Clothes").is_displayed())
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Accessories").is_displayed())
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Art").is_displayed())
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Log in to your customer account").is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to missing UI element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()