import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.remote.webelement import WebElement

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/category-a") # replace with your URL

    def tearDown(self):
        self.driver.quit()

    def test_product_filters(self):
        # Step 1: Open the category page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))

        # Step 2: Wait until products and filters are fully loaded
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))

        # Step 3-4: Apply the "Brand A" checkbox filter using its associated input
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox'][@value='brand-a']")))
        brand_a_checkbox.click()

        # Step 5-6: Confirm it is checked and wait for products to load
        self.assertTrue(brand_a_checkbox.is_selected())
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))

        # Step 7: Verify that the number of product cards is reduced
        initial_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))))
        WebDriverWait(self.driver, 2).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".products .column")) < initial_product_count)

        # Step 8-9: Uncheck the filter and confirm product count is restored
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 20).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".products .column")) == initial_product_count)

        # Step 10-11: Locate the price slider component and move the right slider handle to reduce the maximum price
        price_slider = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='range'][@aria-valuenow='1250']")))
        # Get aria-valuemin, aria-valuemax attributes of the input element and calculate new value for aria-valuenow
        price_slider_min = int(price_slider.get_attribute("aria-valuemin"))
        price_slider_max = int(price_slider.get_attribute("aria-valuemax"))
        new_price_valuenow = 1159
        # Use ActionBuilder to move slider handle
        builder = ActionBuilder(self.driver)
        interaction = Interaction(builder)
        pointer_input = PointerInput(action="pointer", path="/mouse[0]")
        action = builder.move_to(pointer_input, price_slider.location["x"], price_slider.location["y"] + 10).perform().pause(500).move_to(pointer_input, price_slider.location["x"] + (price_slider_max - new_price_valuenow) / 2.5, price_slider.location["y"]).release()
        interaction.perform(action)

        # Step 12-13: Wait for products to load and verify that the number of product cards is reduced
        WebDriverWait(self.driver, 20).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".products .column")) < initial_product_count)
        WebDriverWait(self.driver, 2).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".products .column")) < initial_product_count)

if __name__ == '__main__':
    unittest.main()