import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver

        # Verify Logo
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img")))
        if not logo.is_displayed():
            self.fail("Logo is not visible")

        # Verify Search Box
        search_box = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        if not search_box.is_displayed():
            self.fail("Search box is not visible")

        # Verify Category Links
        for category in ["Category A", "Category B", "Category C"]:
            category_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            if not category_link.is_displayed():
                self.fail(f"{category} link is not visible")
    
        # Verify Best Sellers Section
        best_sellers = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.title.is-4.has-text-centered")))
        if not best_sellers.is_displayed():
            self.fail("Best Sellers section title is not visible")

        # Verify Product A and Product B are visible
        for product in ["Product A", "Product B"]:
            product_element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, product)))
            if not product_element.is_displayed():
                self.fail(f"{product} is not visible")
        
        # Verify Cart Icon
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-button img")))
        if not cart_icon.is_displayed():
            self.fail("Cart icon is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()