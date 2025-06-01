import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation menu
        navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
        self.assertTrue(navigation.is_displayed(), "Navigation menu is not visible")

        # Check search input field
        search_input = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check 'Search' button
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
        self.assertTrue(search_button.is_displayed(), "Search button is not visible")

        # Check for product items
        product_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-item')))
        self.assertGreater(len(product_items), 0, "No product items found")

        # Check 'Add to cart' buttons
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, 'product-box-add-to-cart-button')
        self.assertGreater(len(add_to_cart_buttons), 0, "No 'Add to cart' buttons found")

        # Interact with the 'Search' button
        search_input.send_keys("book")
        search_button.click()

        # Confirm search results are updated (wait for element change/refresh or interaction feedback)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'products-wrapper')))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()