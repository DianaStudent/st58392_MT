import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer is not visible")

        # Check main navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav ul.nav-level-0 li .cat-parent a")))
        except:
            self.fail("Main navigation links are not visible")

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img")))
        except:
            self.fail("Logo is not visible")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        except:
            self.fail("Search input field is not visible")

        # Check cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img[alt='cart']")))
        except:
            self.fail("Cart button is not visible")

        # Check best sellers section title
        try:
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4.has-text-centered")))
        except:
            self.fail("Best Sellers section title is not visible")

        # Check best seller products
        try:
            best_seller_products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
        except:
            self.fail("Best seller products are not visible")

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()