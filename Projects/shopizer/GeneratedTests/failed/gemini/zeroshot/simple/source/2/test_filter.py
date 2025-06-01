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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Accept cookies if the consent banner is present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find the 'All' tab and count products
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and @role='tabpanel']")))
            initial_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and @role='tabpanel']//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
            initial_count = len(initial_products)
        except:
            self.fail("Could not find 'All' tab or count initial products.")

        # Find the 'Tables' tab and click
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and @role='tabpanel']")))
            filtered_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and @role='tabpanel']//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
            filtered_count = len(filtered_products)
        except:
            self.fail("Could not find 'Tables' tab or count filtered products.")

        # Verify that at least one product is displayed after filtering
        if filtered_count == 0:
            self.fail("No products displayed after filtering.")

        # Verify that the product count changed after filtering
        if initial_count == filtered_count:
            self.fail("Product count did not change after filtering.")


if __name__ == "__main__":
    unittest.main()