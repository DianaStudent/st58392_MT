from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify header elements
            header_elements = [
                "//a[contains(@href, '/register') and contains(@class, 'ico-register')]",
                "//a[contains(@href, '/login') and contains(@class, 'ico-login')]",
                "//a[contains(@href, '/wishlist') and contains(@class, 'ico-wishlist')]",
                "//a[contains(@href, '/cart') and contains(@class, 'ico-cart')]"
            ]
            for selector in header_elements:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
            
            # Verify search box
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))

            # Verify product filters
            filter_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'filter-title')))
            price_range_slider = wait.until(EC.visibility_of_element_located((By.ID, 'price-range-slider')))

            # Verify search result products
            product_elements = driver.find_elements(By.CLASS_NAME, 'product-item')
            if not product_elements:
                self.fail("No product items found")

            # Verify footer elements
            footer_elements = [
                "//a[contains(@href, '/contactus')]",
                "//a[contains(@href, '/sitemap')]",
                "//a[contains(@href, '/privacy-notice')]"
            ]
            for selector in footer_elements:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))

        except Exception as e:
            self.fail(f"UI Element not found or visible: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()