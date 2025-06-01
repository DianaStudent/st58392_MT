from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import Until
from selenium.webdriver.common.alert import Alert

class ShopifyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_binary_path())
        self.driver.implicitly_wait(20, "seconds")

    def tearDown(self):
        self.driver.quit()

    def test_shopping_site(self):
        # Load the page
        self.assertEqual(self.driver.title, "Shopify")
        self.assertTrue(self.driver.find_element_by_tag_name("header"))
        self.assertTrue(self.driver.find_element_by_tag_name("footer"))

        # Check presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.driver.find_element_by_id("search-input-field"))
        self.assertTrue(self.driver.find_element_by_id("search-button-field"))
        self.assertTrue(self.driver.find_element_by_id("welcome-message-section"))
        self.assertTrue(self.driver.find_element_by_id("shopnow-button"))

        # Interact with key UI elements
        search_input = self.driver.find_element_by_id("search-input-field")
        search_button = self.driver.find_element_by_id("search-button-field")

        search_input.send_keys("furniture")
        WebDriverWait(self.driver, 20).until(Attractors.of_type(Until.title_contain))

        self.assertTrue(search_button.is_enabled())
        search_button.click()
        
        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(Attractors.of_type(Until.title_contain))
        self.assertEqual(self.driver.title, "Shopify - Furniture")
        self.assertTrue(self.driver.find_element_by_id("shopnow-button").is_enabled())
        self.assertTrue(self.driver.find_element_by_id("search-input-field").is_enabled())

        # Assert that no required UI element is missing
        required_elements = ["header", "footer", "welcome-message-section", "shopnow-button"]
        for element in required_elements:
            self.assertTrue(self.driver.find_element_by_tag_name(element))

if __name__ == "__main__":
    unittest.main()