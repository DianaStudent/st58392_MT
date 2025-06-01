from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Close cookie consent if available
        try:
            cookie_accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_accept_btn.click()
        except:
            pass

        # Select "Tables" tab and verify products
        tables_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Tables']]")))
        tables_tab.click()

        tables_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]/div[@class='row']/div")))
        self.assertGreater(len(tables_products), 0, "No products displayed for 'Tables' filter.")

        # Select "Chairs" tab and verify products
        chairs_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Chairs']]")))
        chairs_tab.click()

        chairs_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]/div[@class='row']/div")))
        self.assertGreater(len(chairs_products), 0, "No products displayed for 'Chairs' filter.")

        # Select "All" tab and verify full list of products
        all_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='All']]")))
        all_tab.click()

        all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]/div[@class='row']/div")))
        self.assertGreater(len(all_products), 0, "No products displayed for 'All' filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()