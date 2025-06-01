import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        # Check header is present and visible
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer is present and visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check navigation links are present and visible
        nav_links = ["/", "/category/tables", "/category/chairs"]
        for link in nav_links:
            nav_item = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            self.assertIsNotNone(nav_item, f"Navigation link {link} is not visible")

        # Check buttons and their visibility
        accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(accept_cookies_button, "Accept cookies button not visible")

        # Interact with the "Accept cookies" button
        accept_cookies_button.click()

        # Verify the "Accept cookies" button is no longer visible or present
        self.assertFalse(self.is_element_present(By.ID, "rcc-confirm-button"), "Accept cookies button is still present after clicking")

        # Assert the presence of input fields in footer for subscription
        subscribe_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        self.assertIsNotNone(subscribe_field, "Subscription input field not visible")

        subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .button")))
        self.assertIsNotNone(subscribe_button, "Subscribe button not visible")

    def is_element_present(self, by, value):
        try:
            self.driver.find_element(by, value)
        except:
            return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()