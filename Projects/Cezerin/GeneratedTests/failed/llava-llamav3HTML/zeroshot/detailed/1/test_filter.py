from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestScenario(unittest.TestCase):
    def setUp(self):
        driver = ChromeDriverManager().create_instance()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_scenario(self):
        # Step 1: Open the category page.
        self.driver.get("http://localhost:3000/category-a")

        # Wait until products and filters are fully loaded.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located([By.XPATH("//*[contains('data-product-name')]")]))

        # Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_filter = self.driver.find_element_by_xpath("//*[contains('label', 'brand-a-filter')]")
        self.assertTrue(brand_a_filter.get_attribute("aria-label").strip() == "Brand A")
        brand_a_filter.click()

        # Confirm it is checked.
        WebDriverWait(self.driver, 2).until(EC.visibility_of_all_elements_located([By.XPATH("//*[contains('data-product-name')]")]))
        product_cards = self.driver.find_elements_by_xpath("//*[contains('data-product-name')]")

        # Verify that the number of visible product cards must change after applying and removing the filter (e.g., 2 → 1 → 2).
        original_product_count = len(product_cards)
        brand_a_filter.click()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_all_elements_located([By.XPATH("//*[contains('data-product-name')]")]))
        new_product_count = len(product_cards)

        self.assertTrue(original_product_count != new_product_count)

        # Uncheck the filter and confirm product count is restored.
        brand_a_filter.click()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_all_elements_located([By.XPATH("//*[contains('data-product-name')]")]))
        product_cards = self.driver.find_elements_by_xpath("//*[contains('data-product-name')]")

        # Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        price_slider = self.driver.find_element_by_css_selector(".price-filter-slider")

        max_price_input = price_slider.find_element_by_css_selector("[aria-label='Maximum']")
        self.assertTrue(max_price_input.get_attribute("aria-valuenow") == "0")
        self.assertTrue(max_price_input.get_attribute("aria-valuemin") == "1159")

        for i in range(2158, 1159, -100):
            price_slider.find_element_by_css_selector("[aria-label='Maximum']").send_keys(str(i))
            WebDriverWait(self.driver, 2).until(EC.visibility_of_all_elements_located([By.XPATH("//*[contains('data-product-name')]")]))
            product_cards = self.driver.find_elements_by_xpath("//*[contains('data-product-name')]")

        # Step 6: Verify that the number of visible product cards must change after applying and removing the filter (e.g., 2 → 1 → 2).
        original_product_count = len(product_cards)
        for i in range(2158, 1159, -100):
            price_slider.find_element_by_css_selector("[aria-label='Maximum']").send_keys(str(i))
            WebDriverWait(self.driver, 2).until(EC.visibility_of_all_elements_located([By.XPATH("//*[contains('data-product-name')]")]))
            product_cards = self.driver.find_elements_by_xpath("//*[contains('data-product-name')]")

        self.assertTrue(original_product_count != len(product_cards))

if __name__ == "__main__":
    unittest.main()