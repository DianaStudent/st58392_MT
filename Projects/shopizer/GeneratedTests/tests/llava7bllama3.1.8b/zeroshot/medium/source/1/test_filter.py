import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFiltering(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def test_filtering(self):
        # Click on the "Tables" tab to filter products
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Chairs']"))
        )
        tables_tab.click()

        # Verify that at least one product appears
        product_count = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-count']"))
        ).text.strip()
        self.assertGreater(int(product_count), 0)

        # Click on the "Chairs" tab to change the filter
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Tables']"))
        )
        chairs_tab.click()

        # Verify that product list is updated
        new_product_count = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-count']"))
        ).text.strip()
        self.assertGreater(int(new_product_count), 0)

        # Click "All" to remove the filter
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='All']"))
        )
        all_tab.click()

        # Confirm that the full list of products is shown
        final_product_count = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-count']"))
        ).text.strip()
        self.assertEqual(int(final_product_count), 4)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()