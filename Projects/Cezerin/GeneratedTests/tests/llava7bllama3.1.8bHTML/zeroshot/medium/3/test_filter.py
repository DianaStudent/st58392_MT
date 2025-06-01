import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceApp(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_category_page_filtering(self):
        # Open the category page
        self.driver.get("your-category-page-url")

        # Apply "Brand A" filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Brand A']")))
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2)  # Wait for UI to update

        # Verify product count change (e.g., from 2 to 1)
        original_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-caption']"))))
        WebDriverWait(self.driver, 2)  # Wait for UI to update
        filtered_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-caption']"))))

        self.assertLess(original_product_count, filtered_product_count)

        # Unapply "Brand A" filter
        brand_a_checkbox.click()

        # Verify original product count is restored (e.g., from 1 to 2)
        WebDriverWait(self.driver, 2)  # Wait for UI to update
        restored_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-caption']"))))

        self.assertEqual(original_product_count, restored_product_count)

        # Locate and apply price slider filter
        price_slider_handle = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='range']")))
        price_slider_handle.send_keys('50')  # Move one of the slider handles to apply a price range filter

        # Verify product count change again
        WebDriverWait(self.driver, 2)  # Wait for UI to update
        filtered_product_count_price_slider = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-caption']"))))

        self.assertLess(original_product_count, filtered_product_count_price_slider)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()