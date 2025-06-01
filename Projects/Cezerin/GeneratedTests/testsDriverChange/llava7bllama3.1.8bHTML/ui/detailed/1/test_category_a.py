import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homepage_elements(self):
        # Load the page
        self.driver.get("http://example.com")  # Replace with your URL

        # Wait for the header to be visible
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
        )
        self.assertTrue(header.is_displayed())

        # Check the presence of key UI elements
        required_elements = [
            ("h1", "category_a"),
            ("button", "Add to Cart"),
            ("a", "View Cart")
        ]

        for element_type, expected_text in required_elements:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f"{element_type}:contains('{expected_text}')"))
                )
            except TimeoutException:
                self.fail(f"Missing required UI element: {element_type}:contains('{expected_text}')")

        # Interact with key UI elements
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button:contains('Add to Cart')"))
        ).click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span:contains('Added to cart')"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()