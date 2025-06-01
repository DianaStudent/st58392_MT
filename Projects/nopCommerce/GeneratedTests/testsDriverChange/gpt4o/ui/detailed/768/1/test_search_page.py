import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not visible.")

        # Check footer elements
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not visible.")

        # Check navigation menu
        nav_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
        self.assertIsNotNone(nav_menu, "Navigation menu is not visible.")

        # Check search box and button
        search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
        self.assertIsNotNone(search_box, "Search box is not visible.")
        self.assertIsNotNone(search_button, "Search button is not visible.")

        # Check product grid presence
        product_grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-grid')))
        self.assertIsNotNone(product_grid, "Product grid is not visible.")

        # Check the presence of advanced search checkbox
        advanced_search_checkbox = wait.until(EC.visibility_of_element_located((By.ID, 'advs')))
        self.assertIsNotNone(advanced_search_checkbox, "Advanced search checkbox is not visible.")

        # Interact with advanced search checkbox
        advanced_search_checkbox.click()
        advanced_search_block = wait.until(EC.visibility_of_element_located((By.ID, 'advanced-search-block')))
        self.assertTrue(advanced_search_block.is_displayed(), "Advanced search block did not appear after clicking the checkbox.")

        # Check the add to cart buttons
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, 'product-box-add-to-cart-button')
        self.assertGreater(len(add_to_cart_buttons), 0, "No add to cart buttons found.")
        for button in add_to_cart_buttons:
            self.assertTrue(button.is_displayed(), "Add to cart button is not visible.")

if __name__ == "__main__":
    unittest.main()