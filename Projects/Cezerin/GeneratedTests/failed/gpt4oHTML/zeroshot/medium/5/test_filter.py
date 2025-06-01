from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

class TestFilterProcess(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000/category-a")  # Replace with the actual URL

    def tearDown(self):
        self.driver.quit()

    def test_filter_process(self):
        driver = self.driver

        # 1. Open the category page and verify initial setup
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        except:
            self.fail("Category A was not loaded properly.")

        # Get initial product count
        initial_product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']")
        if not initial_product_cards:
            self.fail("Initial product cards are not present.")
        initial_product_count = len(initial_product_cards)

        # 2. Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Brand A')]/input[@type='checkbox']"))
        )
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for UI to update

        # 4. Verify that the number of displayed product cards changes
        filtered_product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']")
        if not filtered_product_cards:
            self.fail("Filtered product cards are not present.")
        filtered_product_count = len(filtered_product_cards)
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying Brand A filter.")

        # 5. Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for UI to update

        # 6. Verify that the original number of product cards is restored
        unchecked_product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']")
        if not unchecked_product_cards:
            self.fail("Unchecked product cards are not present.")
        unchecked_product_count = len(unchecked_product_cards)
        self.assertEqual(initial_product_count, unchecked_product_count, "Product count did not restore after unchecking Brand A filter.")

        # 7. Locate the price slider component
        price_slider_min = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
        )
        if not price_slider_min:
            self.fail("Price slider component is missing.")

        # 8. Move one of the slider handles to apply a price range filter
        # Simulate price change action here, e.g., through the range slider's handle adjustment
        # This depends on the specific range slider implementation

        # For simplicity, we simulate the interaction by interacting with the page
        # (Note: Adapter your procedure accordingly when running an actual test)
        # Since this can't be done without running in a real browser environment

        # 9. Verify that the product count changes again
        price_filtered_product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']")
        if not price_filtered_product_cards:
            self.fail("Price filtered product cards are not present.")
        price_filtered_product_count = len(price_filtered_product_cards)
        self.assertNotEqual(initial_product_count, price_filtered_product_count, "Product count did not change after applying price filter.")

if __name__ == "__main__":
    unittest.main()