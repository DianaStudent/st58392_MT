import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Verify header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img")))
            self.assertTrue(logo.is_displayed())
        except:
            self.fail("Logo is not visible.")

        # Verify search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
            self.assertTrue(search_input.is_displayed())
        except:
            self.fail("Search input is not visible.")

        # Verify cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-button img")))
            self.assertTrue(cart_icon.is_displayed())
        except:
            self.fail("Cart icon is not visible.")

        # Verify primary navigation
        try:
            nav_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav")))
            self.assertTrue(nav_links.is_displayed())
        except:
            self.fail("Primary navigation is not visible.")

        # Verify best sellers section
        try:
            best_sellers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4")))
            self.assertTrue(best_sellers.is_displayed())
        except:
            self.fail("Best Sellers section is not visible.")

        # Verify product items
        try:
            product_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product A")))
            self.assertTrue(product_a.is_displayed())
        except:
            self.fail("Product A is not visible.")

        try:
            product_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product B")))
            self.assertTrue(product_b.is_displayed())
        except:
            self.fail("Product B is not visible.")

        # Verify footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
            self.assertTrue(footer.is_displayed())
        except:
            self.fail("Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()