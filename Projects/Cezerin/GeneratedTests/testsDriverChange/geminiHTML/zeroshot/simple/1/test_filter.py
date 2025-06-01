import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CategoryAFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_brand_a(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Get initial number of product cards
        product_cards_initial = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column[class*='is-']")))
        num_product_cards_initial = len(product_cards_initial)

        # Find the Brand A checkbox
        brand_a_checkbox_label = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[contains(text(), 'Brand A')]"))
        )
        brand_a_checkbox = brand_a_checkbox_label.find_element(By.XPATH, "./input[@type='checkbox']")

        # Click the Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Get number of product cards after applying filter
        product_cards_filtered = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column[class*='is-']")))
        num_product_cards_filtered = len(product_cards_filtered)

        # Uncheck the Brand A checkbox
        brand_a_checkbox_label = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[contains(text(), 'Brand A')]"))
        )
        brand_a_checkbox = brand_a_checkbox_label.find_element(By.XPATH, "./input[@type='checkbox']")
        brand_a_checkbox.click()
        time.sleep(2)

        # Get number of product cards after removing filter
        product_cards_unfiltered = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column[class*='is-']")))
        num_product_cards_unfiltered = len(product_cards_unfiltered)

        # Assert that the number of product cards changed after applying and removing the filter
        self.assertNotEqual(num_product_cards_initial, num_product_cards_filtered, "Number of product cards should change after applying filter")
        self.assertEqual(num_product_cards_initial, num_product_cards_unfiltered, "Number of product cards should return to initial after removing filter")

    def test_filter_price_range(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Get initial number of product cards
        product_cards_initial = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column[class*='is-']")))
        num_product_cards_initial = len(product_cards_initial)

        # Assuming a price slider exists and can be manipulated.  This is a placeholder.
        #  A real implementation would require more information about the slider's HTML structure
        #  and how to interact with it (e.g., using ActionChains to drag the slider handle).
        #  For this example, we'll just check if the price filter element exists.

        try:
            price_filter_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter"))
            )
        except:
            self.fail("Price filter element not found")

        # Placeholder for interacting with the price slider.
        # In a real test, you would use ActionChains to drag the slider handle.
        # For example:
        # from selenium.webdriver.common.action_chains import ActionChains
        # slider_handle = driver.find_element(By.CSS_SELECTOR, ".price-filter .slider-handle")
        # actions = ActionChains(driver)
        # actions.drag_and_drop_by_offset(slider_handle, 50, 0).perform() # Move the slider handle
        time.sleep(2)

        # Get number of product cards after applying price filter
        product_cards_filtered = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column[class*='is-']")))
        num_product_cards_filtered = len(product_cards_filtered)

        # Assert that the number of product cards changed after applying the price filter
        self.assertNotEqual(num_product_cards_initial, num_product_cards_filtered, "Number of product cards should change after applying price filter")

if __name__ == "__main__":
    unittest.main()