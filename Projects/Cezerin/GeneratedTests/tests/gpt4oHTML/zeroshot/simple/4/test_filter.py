import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("file:///path_to_local_html_file.html")  # Update this with the path to your HTML file
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_apply_filter(self):
        driver = self.driver

        # Locate and click on the "Brand A" checkbox
        brand_a_checkbox = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title' and text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
        )
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for 2 seconds

        # Verify products change; should see Product A only
        product_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'products')]//div[contains(@class,'column') and contains(@class, 'available')]")
        self.assertEqual(len(product_elements), 1)  # Expect 1 visible product (Product A)

        # Unselect the "Brand A" checkbox
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for 2 seconds

        # Verify products change back to the original state; should see Product A and Product B
        product_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'products')]//div[contains(@class,'column') and contains(@class, 'available')]")
        self.assertEqual(len(product_elements), 2)  # Expect back to 2 visible products (Product A and Product B)

        # Change price filtering (interaction with slider is skipped since there's no slider control in given HTML)
        # We'll simulate this by manually checking the price filter values exist
        price_filter_left = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='column has-text-left']"))
        )
        price_filter_right = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='column has-text-right']"))
        )

        # Validate price filter values
        self.assertEqual(price_filter_left.text, "$950.00")
        self.assertEqual(price_filter_right.text, "$1,250.00")
        
        # Simulate a price range shift to filter out Product A (you would replace this with actual slider interaction)
        dummy_price_change_script = """
        var leftPrice = document.querySelector("div.columns.is-mobile.is-gapless.price-filter-values div.has-text-left");
        leftPrice.textContent = '$967.00';
        """
        driver.execute_script(dummy_price_change_script)
        time.sleep(2)  # Wait for 2 seconds to simulate filter application

        # Verify that only Product B is visible after this price filter simulation
        product_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'products')]//div[contains(@class,'column') and contains(@class, 'available')]")
        self.assertEqual(len(product_elements), 1)  # Expect 1 visible product (Product B)

if __name__ == "__main__":
    unittest.main()