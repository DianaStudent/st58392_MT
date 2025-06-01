from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.url = "http://localhost/"

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Load the homepage
        driver.get(self.url)
        
        # Verify navigation links
        nav_links = ['Home', 'Tables', 'Chairs']
        for link_text in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"Navigation link '{link_text}' is not visible")

        # Verify accept cookies button
        accept_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_button.is_displayed(), "Accept cookies button is not visible")
        
        # Click the accept cookies button
        accept_button.click()
        
        # Check site banner
        banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-block-cover-content")))
        self.assertTrue(banner.is_displayed(), "Site banner is not visible")

        # Verify featured products section
        featured_products_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".section-title-5 h2")))
        self.assertTrue(featured_products_title.is_displayed(), "Featured Products title is not visible")
        self.assertEqual(featured_products_title.text, "Featured Products", "Featured Products title text mismatch")

        # Verify product images and action buttons
        product_images = driver.find_elements(By.CSS_SELECTOR, ".product-img a img")
        self.assertGreater(len(product_images), 0, "No product images found")
        
        for product in product_images:
            self.assertTrue(product.is_displayed(), "Product image is not visible")

        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        self.assertGreater(len(add_to_cart_buttons), 0, "No Add to Cart buttons found")
        
        for button in add_to_cart_buttons:
            self.assertTrue(button.is_displayed(), "Add to Cart button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()