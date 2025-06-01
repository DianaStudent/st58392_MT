from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header"))), "Header is not visible")

        # Check footer
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer"))), "Footer is not visible")

        # Check navigation links
        nav_links = ['Category A', 'Category B', 'Category C']
        for link_text in nav_links:
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text))), f"{link_text} link is not visible")

        # Check search input
        search_input = driver.find_element(By.CSS_SELECTOR, 'input.search-input')
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check sort select
        sort_select = driver.find_element(By.CSS_SELECTOR, 'select')
        self.assertTrue(sort_select.is_displayed(), "Sort select is not visible")

        # Check buttons
        cart_button = driver.find_element(By.CSS_SELECTOR, 'span.cart-button')
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Check product links
        product_links = driver.find_elements(By.CSS_SELECTOR, '.products a')
        self.assertGreater(len(product_links), 0, "Product links are not visible")

        # Check interaction with key UI elements
        cart_button.click()
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-cart'))), "Mini cart is not visible after clicking cart button")

if __name__ == "__main__":
    unittest.main()