from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_home_page(self):
        # Open the home page
        self.driver.get("http://max/")

        # Check that structural elements are visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check the presence and visibility of input fields, buttons, labels, and sections
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#newsletter-subscribe-button")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".block .title")))

        # Interact with key UI elements (e.g., click buttons)
        self.driver.find_element(By.CSS_SELECTOR, "#newsletter-subscribe-button").click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#subscribe-loading-progress")))

        # Assert that no required UI element is missing
        elements = [
            ("header", By.CSS_SELECTOR),
            ("footer", By.CSS_SELECTOR),
            ("newsletter-email", "id"),
            ("#newsletter-subscribe-button", CSS_SELECTOR),
            (".block .title", CSS_SELECTOR)
        ]

        for selector, locator_type in elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator_type, selector)))
            except TimeoutException:
                self.fail(f"Missing required element: {selector}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()