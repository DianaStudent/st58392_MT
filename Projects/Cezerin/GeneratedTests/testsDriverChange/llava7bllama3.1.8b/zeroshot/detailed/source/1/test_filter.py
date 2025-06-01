import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_filter_brand_a_and_price_slider(self):
        # Wait until products and filters are fully loaded
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid")))

        # Locate the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='filter_brand_A'] input")))
        
        # Apply the "Brand A" checkbox filter
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(lambda x: len(x.find_elements_by_css_selector(".product-grid .product-card")) < len(self.driver.find_elements_by_css_selector(".product-grid .product-card")))
        self.assertTrue(brand_a_checkbox.is_selected())

        # Wait and verify that the number of product cards is reduced
        WebDriverWait(self.driver, 2).until(lambda x: len(x.find_elements_by_css_selector(".product-grid .product-card")) == 1)

        # Uncheck the filter
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(lambda x: len(x.find_elements_by_css_selector(".product-grid .product-card")) > 1)

        # Locate the price slider component
        price_slider = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-slider")))
        
        # Move the right slider handle to reduce the maximum price
        price_slider.find_elements_by_css_selector(".price-handle")[1].click()
        WebDriverWait(self.driver, 2).until(lambda x: int(x.execute_script("return arguments[0].getAttribute('aria-valuenow');", x.find_element_by_xpath("//input[@type='range']"))) == 1159)

        # Wait and verify that the number of product cards is reduced
        WebDriverWait(self.driver, 2).until(lambda x: len(x.find_elements_by_css_selector(".product-grid .product-card")) < len(self.driver.find_elements_by_css_selector(".product-grid .product-card")))

if __name__ == "__main__":
    unittest.main()