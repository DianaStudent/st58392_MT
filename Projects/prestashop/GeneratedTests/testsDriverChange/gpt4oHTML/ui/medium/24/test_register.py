import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Confirm presence and visibility of header
        try:
            header = self.wait.until(EC.presence_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except Exception as e:
            self.fail(f"Header missing: {str(e)}")
        
        # Confirm presence and visibility of navigation links in top menu
        try:
            home_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            clothes_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Clothes")))
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible")

            accessories_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Accessories")))
            self.assertTrue(accessories_link.is_displayed(), "Accessories link is not visible")

            art_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Art")))
            self.assertTrue(art_link.is_displayed(), "Art link is not visible")
        except Exception as e:
            self.fail(f"Navigation links missing: {str(e)}")

        # Confirm presence and visibility of form elements
        try:
            firstname_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
            self.assertTrue(firstname_input.is_displayed(), "First name input is not visible")

            lastname_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
            self.assertTrue(lastname_input.is_displayed(), "Last name input is not visible")

            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")
        except Exception as e:
            self.fail(f"Form inputs missing: {str(e)}")
        
        # Confirm presence and visibility of the submit button
        try:
            submit_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
            self.assertTrue(submit_button.is_displayed(), "Submit button is not visible")
        except Exception as e:
            self.fail(f"Submit button missing: {str(e)}")

        # Interact with an element, e.g., fill in the first name and check if UI allows it
        try:
            firstname_input.send_keys("John")
            submit_button.click()
            # Assuming there is a UI update or message after submission
            confirmation_element = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Thank you')]")))
            self.assertTrue(confirmation_element.is_displayed(), "Confirmation message is not visible")
        except Exception as e:
            self.fail(f"Error interacting with elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()