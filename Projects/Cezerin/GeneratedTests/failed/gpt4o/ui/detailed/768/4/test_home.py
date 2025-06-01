from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        # Ensure header is present and visible
        header = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Ensure footer is present and visible
        footer = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check search input field
        search_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-input"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

        # Check navigation links
        navigation_links = driver.find_elements(By.CSS_SELECTOR, ".nav-level-0 li a")
        self.assertGreater(len(navigation_links), 0, "No navigation links found.")
        for link in navigation_links:
            self.assertTrue(link.is_displayed(), f"Navigation link '{link.text}' is not visible.")

        # Check best sellers products
        best_sellers = driver.find_elements(By.CSS_SELECTOR, ".products .product-name")
        self.assertGreater(len(best_sellers), 0, "No products found in Best Sellers.")
        for product in best_sellers:
            self.assertTrue(product.is_displayed(), f"Product '{product.text}' is not visible.")

        # Interact with search icon button
        search_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-icon-search"))
        )
        search_icon.click()
        
        # Verify interaction (possibly by checking a resulting element)
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible after clicking search icon.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()