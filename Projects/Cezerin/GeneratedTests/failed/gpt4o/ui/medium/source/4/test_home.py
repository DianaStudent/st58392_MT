from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomepageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for navigation elements
        navigation_links = [
            (By.CSS_SELECTOR, "a[href='/category-a']"),
            (By.CSS_SELECTOR, "a[href='/category-b']"),
            (By.CSS_SELECTOR, "a[href='/category-c']")
        ]

        for selector in navigation_links:
            nav_element = wait.until(EC.visibility_of_element_located(selector))
            if not nav_element:
                self.fail(f"Navigation element {selector} not present")

        # Check for logo
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img")))
        if not logo:
            self.fail("Logo not present")

        # Check for search input
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        if not search_input:
            self.fail("Search input not present")

        # Check for cart button
        cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-button img")))
        if not cart_button:
            self.fail("Cart button not present")

        # Interact with the search input and verify UI update
        search_input.send_keys("Shoes")
        driver.find_element(By.CSS_SELECTOR, "img.search-icon-search").click()

        # Verify the presence of the banner
        banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.image-gallery-image a img")))
        if not banner:
            self.fail("Banner not present")

        # Check for 'BEST SELLERS' section
        best_sellers_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.title.is-4")))
        if not best_sellers_title:
            self.fail("'BEST SELLERS' section is not present")        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()