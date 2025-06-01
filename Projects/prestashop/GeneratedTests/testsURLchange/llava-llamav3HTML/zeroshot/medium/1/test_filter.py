import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestProductFiltering(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver instance
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Clean up the WebDriver instance
        self.driver.quit()

    def test_product_filtering(self):
        try:
            # Open the home page
            self.driver.get('http://localhost:8080/en/')

            # Navigate to a product category
            WebDriverWait(self.driver, 20).until(
                lambda x: 'data-categories' in x.title_attribute
            )

            # On the category page, wait for the filter sidebar to be present
            WebDriverWait(self.driver, 20).until(
                lambda x: 'data-categories' in x.title_attribute
            )

            # Select a checkbox filter using label-based selection
            product_filter = self.driver.find_element_by_label('Pack Mug + Framed poster')
            product_filter.click()

            # Wait for the page to update, and verify that the number of visible product items is reduced
            WebDriverWait(self.driver, 20).until(
                lambda x: int(x.title_attribute) < 1,
            )

            # Click the "Clear all" button to remove filters
            clear_all_button = self.driver.find_element_by_name('data-clear-all')
            clear_all_button.click()

            # Verify that the number of products returns to the original count
            WebDriverWait(self.driver, 20).until(
                lambda x: int(x.title_attribute) == 0,
            )

        except Exception as e:
            self.fail(str(e))

if __name__ == '__main__':
    unittest.main()