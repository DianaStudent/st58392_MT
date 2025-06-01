from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductMarket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_ui_elements(self):
        # Wait for the header to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='header']"))
        )

        # Check that the main UI components are present and visible
        elements = [
            ("header", "xpath", "//div[@class='header']"),
            ("footer", "xpath", "//div[@class='footer']"),
            ("product-listing", "xpath", "//div[@class='product-listing']"),
            ("add-to-cart-button", "xpath", "//button[@id='addToCartButton']"),
        ]

        for name, locator_type, locator in elements:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((locator_type, locator))
            )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()