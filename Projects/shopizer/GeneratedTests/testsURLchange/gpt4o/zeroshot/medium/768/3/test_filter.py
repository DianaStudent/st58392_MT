import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ProductFilterTest(unittest.TestCase):
    URL = "http://localhost/"

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass

        # Filter by Tables
        tables_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@role='tab']//h4[text()='Tables']")))
        tables_tab.click()

        # Verify at least one product is displayed
        tables_products = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")))
        if not tables_products:
            self.fail("No tables products displayed after filter")

        # Filter by Chairs
        chairs_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@role='tab']//h4[text()='Chairs']")))
        chairs_tab.click()

        # Verify product list is updated
        chairs_products = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")))
        if not chairs_products:
            self.fail("No chairs products displayed after filter")

        # Filter by All
        all_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@role='tab']//h4[text()='All']")))
        all_tab.click()

        # Verify all products are displayed
        all_products = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")))
        if not all_products:
            self.fail("No products displayed after removing filter")


if __name__ == "__main__":
    unittest.main()