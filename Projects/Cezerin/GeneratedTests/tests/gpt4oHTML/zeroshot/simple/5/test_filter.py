import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("URL_OF_THE_PAGE")  # Replace with the actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_brand_a_filter_and_price_slider(self):
        # Apply "Brand A" filter
        brand_a_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Brand A']/input[@type='checkbox']"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Validate product count after "Brand A" filter applied
        product_cards_after_brand_a = self.driver.find_elements(By.CSS_SELECTOR, "div.products > div.column")
        initial_count_after_brand_a = len(product_cards_after_brand_a)
        self.assertEqual(initial_count_after_brand_a, 1, "Product count should be 1 after applying 'Brand A' filter")

        # Uncheck "Brand A" filter
        brand_a_checkbox.click()

        # Use interactive price slider (dummy implementation as there is no slider HTML in provided data)
        # Assume a method to set price in accordance with DOM interaction, here's a placeholder - adjust as necessary
        # slider_element = self.wait.until(...)
        # ActionChains(self.driver).click_and_hold(slider_element).move_by_offset(...).release().perform()
        time.sleep(2)

        # Validate product count after changing price filter
        product_cards_after_price_filter = self.driver.find_elements(By.CSS_SELECTOR, "div.products > div.column")
        final_count_after_price_filter = len(product_cards_after_price_filter)
        self.assertNotEqual(final_count_after_price_filter, initial_count_after_brand_a,
                            "Product count should change after removing filter") 

        # Re-check product cards count - should go back to original
        # Re-apply brand A filter
        brand_a_checkbox.click()
        time.sleep(2)
        
        product_cards_after_reapply = self.driver.find_elements(By.CSS_SELECTOR, "div.products > div.column")
        final_count_after_reapply = len(product_cards_after_reapply)
        self.assertEqual(final_count_after_reapply, 1,
                         "Product count should be back to 1 after re-applying 'Brand A' filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()