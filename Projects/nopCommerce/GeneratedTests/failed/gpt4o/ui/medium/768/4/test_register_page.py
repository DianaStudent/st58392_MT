from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Verify presence and visibility of header elements
            header_links = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links")))
            self.assertIsNotNone(header_links)

            # Verify navigation links
            for link_text in ["Register", "Log in", "Wishlist", "Shopping cart"]:
                self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text))))

            # Verify presence and visibility of the form fields
            for field_id in ["FirstName", "LastName", "Email", "Password", "ConfirmPassword"]:
                self.assertIsNotNone(self.wait.until(EC.visibility_of_element_located((By.ID, field_id))))

            # Verify presence and visibility of buttons
            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
            self.assertIsNotNone(register_button)

            # Interact with an element
            register_button.click()

            # Verify UI updates or error messages (checking for a validation message)
            email_validation = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".field-validation-valid[data-valmsg-for='Email']"))
            )
            self.assertIsNotNone(email_validation)

        except Exception as e:
            self.fail(f"UI test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()