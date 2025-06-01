from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_art_page_elements(self):
        # Navigate to the Art page
        self.driver.get("http://localhost:8080/en/9-art")

        # Wait for the main content area to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-content"))
        )

        # Check if the header is present and visible
        header = self.driver.find_element(By.TAG_NAME, "header")
        self.assertTrue(header.is_displayed())

        # Check if the navigation menu items are present and visible
        nav_menu_items = self.driver.find_elements(By.CSS_SELECTOR, ".nav-menu-item")
        self.assertGreater(len(nav_menu_items), 0)

        # Check if the product images are present and visible
        product_images = self.driver.find_elements(By.CSS_SELECTOR, ".product-image")
        self.assertGreater(len(product_images), 0)

        # Interact with a button to confirm UI reaction
        buy_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#buy-button"))
        )
        buy_button.click()

        # Assert that the page does not throw any errors after clicking the button
        self.assertFalse(self.driver.page_source.find("Error"))

if __name__ == "__main__":
    unittest.main()