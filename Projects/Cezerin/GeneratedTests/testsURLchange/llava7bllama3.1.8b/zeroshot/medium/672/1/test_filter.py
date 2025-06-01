import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMediaFilterApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_media_filter_app(self):
        # Open the category page
        self.driver.get("http://localhost:3000/category-a")

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Brand A']"))
        )
        brand_a_checkbox.click()

        # Wait 2 seconds to allow the UI to update
        import time
        time.sleep(2)

        # Verify that the number of displayed product cards changes
        initial_product_cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card']"))
        )
        self.assertGreater(len(initial_product_cards), 0)
        brand_a_applied = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card'][contains(text(), 'Brand A')]"))
        )
        self.assertEqual(len(brand_a_applied), len(initial_product_cards) - 1)

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()

        # Wait 2 seconds to allow the UI to update
        time.sleep(2)

        # Verify that the original number of product cards is restored
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card']"))
        )
        self.assertEqual(len(initial_product_cards), len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card']")))))

        # Locate the price slider component
        price_slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='range']"))
        )

        # Move one of the slider handles to apply a price range filter
        price_slider.send_keys(50)

        # Verify that the product count changes again
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card']"))
        )
        self.assertGreater(len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card']")))), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()