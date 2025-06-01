from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def get_product_count(self):
        """Counts the number of product elements displayed."""
        product_elements = self.driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        return len(product_elements)

    def test_product_filter(self):
        # Accept cookies if present
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 1. Open the home page.
        # Implicitly done in setUp

        # Get initial product count
        initial_product_count = self.get_product_count()
        self.assertGreater(initial_product_count, 0, "Initial product count should be greater than 0")

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tables"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        tables_product_count = self.get_product_count()
        self.assertGreater(tables_product_count, 0, "Tables product count should be greater than 0")

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Chairs"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        chairs_product_count = self.get_product_count()
        self.assertGreater(chairs_product_count, 0, "Chairs product count should be greater than 0")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count should change after filtering")

        # 6. Click "All" to remove the filter.
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "All"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        final_product_count = self.get_product_count()
        self.assertGreater(final_product_count, 0, "Final product count should be greater than 0")
        self.assertEqual(initial_product_count, final_product_count, "Product count should return to initial count after removing filter")


if __name__ == "__main__":
    unittest.main()