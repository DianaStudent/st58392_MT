import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        # Set up the ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://yourwebsite.com/category-a")

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check the header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertIsNotNone(header, "Header not found or not visible")

            # Check the search box
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
            self.assertIsNotNone(search_input, "Search input not found or not visible")

            # Check Category A link
            category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            self.assertIsNotNone(category_a_link, "Category A link not found or not visible")
        
            # Check Subcategories
            subcategory_1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1')))
            self.assertIsNotNone(subcategory_1, "Subcategory 1 link not found or not visible")

            subcategory_2 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 2')))
            self.assertIsNotNone(subcategory_2, "Subcategory 2 link not found or not visible")

            subcategory_3 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 3')))
            self.assertIsNotNone(subcategory_3, "Subcategory 3 link not found or not visible")

            # Check the cart button
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
            self.assertIsNotNone(cart_button, "Cart button not found or not visible")

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        # Close the ChromeDriver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()