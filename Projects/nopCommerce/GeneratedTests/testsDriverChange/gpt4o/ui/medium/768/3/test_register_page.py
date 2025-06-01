import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence_and_visiblity(self):
        driver = self.driver
        
        # Check navigation links
        nav_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]
        for locator in nav_links:
            self.assertTrue(
                self.wait.until(EC.visibility_of_element_located(locator)),
                f"Navigation link {locator[1]} not visible"
            )

        # Check form fields
        form_fields = [
            (By.ID, "FirstName"),
            (By.ID, "LastName"),
            (By.ID, "Email"),
            (By.ID, "Password"),
            (By.ID, "ConfirmPassword")
        ]
        for field in form_fields:
            self.assertTrue(
                self.wait.until(EC.visibility_of_element_located(field)),
                f"Form field with ID {field[1]} not visible"
            )

        # Check buttons
        self.assertTrue(
            self.wait.until(EC.visibility_of_element_located((By.ID, "register-button"))),
            "Register button not visible"
        )

        # Interact with an element
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("test")
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-box-button")))
        search_button.click()

        # Verify interaction leads to expected behavior
        self.assertTrue(
            self.wait.until(EC.url_contains("/search?q=test")),
            "Search functionality did not redirect correctly"
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()