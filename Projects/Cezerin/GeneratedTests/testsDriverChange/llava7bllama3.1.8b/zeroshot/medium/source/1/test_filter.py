import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFilterMedium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/category-a')

    def tearDown(self):
        self.driver.quit()

    def test_filter_medium(self):
        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Brand A']")))
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(EC.staleness_of(brand_a_checkbox))

        # Verify that the number of displayed product cards changes
        original_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-card']"))
        WebDriverWait(self.driver, 20).until(EC.staleness_of(self.driver.find_element(By.XPATH, "//div[@class='product-card']")))
        filtered_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-card']"))
        self.assertGreater(filtered_product_count, original_product_count)

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(EC.staleness_of(brand_a_checkbox))

        # Verify that the original number of product cards is restored
        WebDriverWait(self.driver, 20).until(EC.staleness_of(self.driver.find_element(By.XPATH, "//div[@class='product-card']")))
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-card']")), original_product_count)

        # Locate the price slider component
        price_slider = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='range']")))

        # Move one of the slider handles to apply a price range filter
        price_slider.send_keys('10')

        # Verify that the product count changes again
        WebDriverWait(self.driver, 20).until(EC.staleness_of(self.driver.find_element(By.XPATH, "//div[@class='product-card']")))
        self.assertGreater(len(self.driver.find_elements(By.XPATH, "//div[@class='product-card']")), filtered_product_count)

if __name__ == '__main__':
    unittest.main()