from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFilter(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        # Wait for filter sidebar to appear
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section[data-name='FilterSidebar']"))
        )

        # Select a checkbox filter by its label text
        checkbox_label = self.driver.find_element(By.XPATH, "//label[@data-name='price-range-filter']")
        checkbox_button = checkbox_label.find_element(By.TAG_NAME, 'input')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@data-name='price-range-filter']//input"))
        )
        checkbox_button.click()

        # Apply filter and wait for page to load
        self.driver.find_element(By.CSS_SELECTOR, "button[data-name='apply-filters']").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))
        )

        # Get initial number of visible products
        initial_products = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))

        # Select another checkbox filter by its label text
        checkbox_label2 = self.driver.find_element(By.XPATH, "//label[@data-name='category-filter']")
        checkbox_button2 = checkbox_label2.find_element(By.TAG_NAME, 'input')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@data-name='category-filter']//input"))
        )
        checkbox_button2.click()

        # Apply filter and wait for page to load
        self.driver.find_element(By.CSS_SELECTOR, "button[data-name='apply-filters']").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))
        )

        # Get final number of visible products
        final_products = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))

        # Verify that the number of visible product items has changed
        self.assertNotEqual(initial_products, final_products)

    def test_remove_filter(self):
        # Wait for filter sidebar to appear
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section[data-name='FilterSidebar']"))
        )

        # Select a checkbox filter by its label text
        checkbox_label = self.driver.find_element(By.XPATH, "//label[@data-name='price-range-filter']")
        checkbox_button = checkbox_label.find_element(By.TAG_NAME, 'input')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@data-name='price-range-filter']//input"))
        )
        checkbox_button.click()

        # Apply filter and wait for page to load
        self.driver.find_element(By.CSS_SELECTOR, "button[data-name='apply-filters']").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))
        )

        # Get initial number of visible products
        initial_products = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))

        # Remove filter and wait for page to load
        self.driver.find_element(By.XPATH, "//label[@data-name='price-range-filter']//input").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))
        )

        # Get final number of visible products
        final_products = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))

        # Verify that the number of visible product items has changed
        self.assertEqual(initial_products, final_products)

if __name__ == "__main__":
    unittest.main()