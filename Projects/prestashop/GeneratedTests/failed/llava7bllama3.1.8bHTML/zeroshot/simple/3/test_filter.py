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
        # Wait for the filter sidebar to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-name='Filter']")))

        # Select a checkbox filter by its label text
        filter_checkbox = self.driver.find_element(By.XPATH, "//label[@class='custom-checkbox__label' and contains(text(), 'Vector graphics')]")
        filter_checkbox.click()

        # Wait for the products to update after applying the filter
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-name='Product']")))

        # Verify that the number of visible product items changes
        initial_product_count = len(self.driver.find_elements(By.XPATH, "//div[@data-name='Product']"))
        self.assertGreater(initial_product_count, 0)

        # Apply another filter to test removing filters
        filter_checkbox_2 = self.driver.find_element(By.XPATH, "//label[@class='custom-checkbox__label' and contains(text(), 'Framed poster')]")
        filter_checkbox_2.click()

        # Wait for the products to update after applying the second filter
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-name='Product']")))

        # Verify that the number of visible product items changes again
        final_product_count = len(self.driver.find_elements(By.XPATH, "//div[@data-name='Product']"))
        self.assertLessEqual(final_product_count, initial_product_count)

if __name__ == "__main__":
    unittest.main()