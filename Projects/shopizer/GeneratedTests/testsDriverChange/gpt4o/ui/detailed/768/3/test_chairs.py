import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService

class WebsiteUITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Helper for checking visibility
        def is_visible(locator):
            try:
                return WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(locator)
                )
            except TimeoutException:
                self.fail(f"Element {locator} not visible.")

        # Check structural elements
        self.assertTrue(is_visible((By.CSS_SELECTOR, "header.header-area")))
        self.assertTrue(is_visible((By.CSS_SELECTOR, "footer.footer-area")))
        
        # Check navigation bar
        self.assertTrue(is_visible((By.LINK_TEXT, "Home")))
        self.assertTrue(is_visible((By.LINK_TEXT, "Tables")))
        self.assertTrue(is_visible((By.LINK_TEXT, "Chairs")))

        # Check cart button
        self.assertTrue(is_visible((By.CSS_SELECTOR, "button.icon-cart")))
        
        # Check login/register links
        self.assertTrue(is_visible((By.LINK_TEXT, "Login")))
        self.assertTrue(is_visible((By.LINK_TEXT, "Register")))

        # Check cookie consent button
        cookie_button = is_visible((By.ID, "rcc-confirm-button"))
        self.assertIsNotNone(cookie_button)
        
        # Interact with buttons to check for visual change
        cookie_button.click()  # Accept cookies
        # Verify button click worked visually if applicable; possibly by checking button disappearance or state change

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()