from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter_process(self):
        driver = self.driver

        # Accept cookies if the button is present
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            if accept_cookies:
                accept_cookies.click()
        except:
            pass

        # Click on "Tables" tab
        tables_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']")))
        self.assertIsNotNone(tables_tab, "Tables tab not found")
        tables_tab.click()

        # Verify at least one product is shown under "Tables"
        tables_products = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='tabpanel' and @class='fade tab-pane active show']//div[@class='product-wrap-2']")))
        self.assertTrue(len(tables_products) > 0, "No products displayed for Tables filter")

        # Click on "Chairs" tab
        chairs_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']")))
        self.assertIsNotNone(chairs_tab, "Chairs tab not found")
        chairs_tab.click()

        # Verify product list is updated for "Chairs"
        chairs_products = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='tabpanel' and @class='fade tab-pane active show']//div[@class='product-wrap-2']")))
        self.assertTrue(len(chairs_products) > 0, "No products displayed for Chairs filter")
        self.assertNotEqual(len(tables_products), len(chairs_products), "Product list did not update after Chairs filter")

        # Click on "All" tab
        all_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']")))
        self.assertIsNotNone(all_tab, "All tab not found")
        all_tab.click()

        # Confirm full list of products is shown
        all_products = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='tabpanel' and @class='fade tab-pane active show']//div[@class='product-wrap-2']")))
        self.assertTrue(len(all_products) > 0, "No products displayed for All filter")
        self.assertGreater(len(all_products), len(chairs_products), "Product list did not update after removing filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()