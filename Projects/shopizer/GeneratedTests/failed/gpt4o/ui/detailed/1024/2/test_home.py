from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        self.assertTrue(header.is_displayed(), "Header is not displayed")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not displayed")

        # Check navigation links
        links = {
            "Home": "/",
            "Tables": "/category/tables",
            "Chairs": "/category/chairs"
        }
        for text, link in links.items():
            element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
            self.assertIn(link, element.get_attribute("href"), f"{text} link is incorrect or not visible")

        # Check input fields
        subscribe_email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .email")))
        self.assertTrue(subscribe_email_input.is_displayed(), "Subscribe email input is not visible")

        # Check buttons
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
        
        # Check visible sections
        featured_products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-area")))
        self.assertTrue(featured_products.is_displayed(), "Featured products section is not visible")

        # Interact with elements
        accept_cookies_button.click()

        # Verify UI reacts visually
        self.assertFalse(accept_cookies_button.is_displayed(), "Accept cookies button did not disappear after clicking")

    def tearDown(self):
        # Tear down the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()