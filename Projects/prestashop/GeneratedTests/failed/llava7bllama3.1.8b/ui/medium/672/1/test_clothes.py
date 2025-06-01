from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_page_loaded(self):
        # Wait for navigation links to appear
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[role='navigation']")))
        
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        self.assertGreater(len(nav_links), 0)
        self.assertIn("MEN'S CLOTHING", self.driver.page_source)

    def test_add_to_cart_button(self):
        # Wait for add to cart button to appear
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Add to cart']")))
        
        # Click the add to cart button and verify that it updates visually
        add_to_cart_button.click()
        self.assertIn("Added to cart", self.driver.page_source)

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])