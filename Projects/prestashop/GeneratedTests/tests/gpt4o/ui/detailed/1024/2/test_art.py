import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check main navigation links
        nav_links = {
            "Home": "a[href='http://localhost:8080/en/']",
            "Clothes": "a[href='http://localhost:8080/en/3-clothes']",
            "Accessories": "a[href='http://localhost:8080/en/6-accessories']",
            "Art": "a[href='http://localhost:8080/en/9-art']"
        }

        for link_text, selector in nav_links.items():
            link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")

        # Check login link
        login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        # Check register link
        register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Check search input field
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")

        # Check total products label
        total_products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".total-products p")))
        self.assertTrue(total_products.is_displayed(), "Total products label is not visible")

        # Check sort by dropdown
        sort_by_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products-sort-order button")))
        self.assertTrue(sort_by_dropdown.is_displayed(), "Sort by dropdown is not visible")

        # Check product list
        products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#js-product-list .products")))
        self.assertTrue(products.is_displayed(), "Product list is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()