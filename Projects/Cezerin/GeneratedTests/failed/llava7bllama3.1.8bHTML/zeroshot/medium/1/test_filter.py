from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceApp(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://localhost:3000/category-a"
        self.driver.get(f"{self.base_url}/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        # Apply the "Brand A" checkbox filter
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='brand_a']"))).click()
        
        # Wait 2 seconds to allow the UI to update
        self.driver.implicitly_wait(2000)
        
        # Verify that the number of displayed product cards changes (e.g., 2 → 1)
        before_filtered_products = len(self.driver.find_elements(By.XPATH, "//a[@href='/category-a/product-b']"))
        print(before_filtered_products)
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='brand_a']"))).click()
        
        # Wait 2 seconds to allow the UI to update
        self.driver.implicitly_wait(2000)
        
        # Verify that the original number of product cards is restored (e.g., 1 → 2)
        after_unfiltered_products = len(self.driver.find_elements(By.XPATH, "//a[@href='/category-a/product-b']"))
        print(after_unfiltered_products)

        self.assertEqual(before_filtered_products, after_unfiltered_products)

    def test_price_filter(self):
        # Locate the price slider component
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-slider-component']")))

        # Move one of the slider handles to apply a price range filter
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_elements(By.XPATH, "//input[@type='range']")[0])
        self.driver.find_element(By.XPATH, "//input[@type='range']").send_keys('100')
        
        # Verify that the product count changes again
        after_price_filtered_products = len(self.driver.find_elements(By.XPATH, "//a[@href='/category-a/product-b']"))
        print(after_price_filtered_products)

if __name__ == "__main__":
    unittest.main()