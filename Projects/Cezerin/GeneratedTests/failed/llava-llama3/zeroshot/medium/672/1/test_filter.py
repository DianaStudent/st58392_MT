from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class TestCategoryAFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter_brand_a(self):
        # Open the category page
        url = "http://localhost:3000/category-a"
        self.driver.get(url)

        # Locate and apply the  "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='brand']"))))
        brand_a_checkbox.click()

        sleep(2)

        # Verify that the number of displayed product cards changes (e.g., 2 → 1)
        product_cards_count = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'product-cards')]/*[contains(text(), 'Product A')]"))))

    def test_filter_price_range(self):
        # Move one of the slider handles to apply a price range filter
        price_slider = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='price-slider']")))
        slider_handle = self.driver.find_element_by_css_selector('input.price-slider')
```