import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")

    def test_apply_product_filter(self):
        driver = self.driver

        # Wait for "Brand A" checkbox and click it
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='Brand A']/input"))
            )
            brand_a_checkbox.click()
            sleep(2)  # wait to see the change visually

            # Verify the number of visible products after filtering
            products_after_filter = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products_after_filter), 1)

            # Uncheck "Brand A" filter
            brand_a_checkbox.click()
            sleep(2)  # wait to see the change visually

            # Verify the number of visible products after removing the filter
            products_after_removal = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products_after_removal), 2)

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()