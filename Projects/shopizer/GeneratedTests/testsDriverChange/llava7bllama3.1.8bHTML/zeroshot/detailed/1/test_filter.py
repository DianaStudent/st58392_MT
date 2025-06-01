from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Replace with your base url

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tabs")))

        tables_tab = self.driver.find_element(By.LINK_TEXT, "Tables")
        tables_tab.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid .card-body")))

        initial_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-grid .card-body"))
        self.assertGreaterEqual(initial_product_count, 1)

        chairs_tab = self.driver.find_element(By.LINK_TEXT, "Chairs")
        chairs_tab.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid .card-body")))

        new_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-grid .card-body"))
        self.assertGreater(new_product_count, initial_product_count)
        self.assertNotEqual(set(initial_product_count), set(new_product_count))

        all_tab = self.driver.find_element(By.LINK_TEXT, "All")
        all_tab.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid .card-body")))

        final_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-grid .card-body"))
        self.assertGreater(final_product_count, new_product_count)