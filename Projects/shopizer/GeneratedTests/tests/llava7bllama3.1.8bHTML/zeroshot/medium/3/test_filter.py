import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopizer(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000")  # replace with your URL

    def tearDown(self):
        self.driver.quit()

    def test_filtering(self):
        # Click on the "Tables" tab to filter products.
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Tables']"))
        )
        tables_tab.click()

        # Verify that at least one product appears.
        self.verify_product_count(1)

        # Click on the "Chairs" tab to change the filter.
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Chairs']"))
        )
        chairs_tab.click()

        # Verify that product list is updated.
        self.verify_product_count(1)

        # Click "All" to remove the filter.
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='All']"))
        )
        all_tab.click()

        # Confirm that the full list of products is shown.
        self.verify_product_count(4)

    def verify_product_count(self, expected_count):
        product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-name='product-list']"))
        )
        self.assertEqual(len(product_list.find_elements(By.TAG_NAME, 'li')), expected_count)

if __name__ == "__main__":
    unittest.main()