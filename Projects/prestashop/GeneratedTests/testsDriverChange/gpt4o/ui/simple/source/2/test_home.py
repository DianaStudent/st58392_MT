import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check if header elements are present and visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)
        except Exception:
            self.fail("Header not found or not visible")

        # Verify visibility of navigation links
        try:
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))))
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))))
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Cart"))))
        except Exception:
            self.fail("Navigation links not found or not visible")

        # Check visibility of popular products section
        try:
            popular_products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))
            self.assertIsNotNone(popular_products)
        except Exception:
            self.fail("Popular products section not found or not visible")

        # Verify main carousel is present and visible
        try:
            carousel = wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
            self.assertIsNotNone(carousel)
        except Exception:
            self.fail("Carousel not found or not visible")

        # Check visibility of search form
        try:
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            search_input = search_widget.find_element(By.NAME, "s")
            self.assertTrue(search_input.is_displayed())
        except Exception:
            self.fail("Search form not found or not visible")

        # Check footer presence
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertIsNotNone(footer)
        except Exception:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()