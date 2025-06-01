from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header is visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not visible.")

        # Verify footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible.")

        # Check presence of main elements like navigation menu
        navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertIsNotNone(navigation, "Navigation is not visible.")

        # Verify search input field is present and visible
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertIsNotNone(search_input, "Search input field is not visible.")

        # Verify the presence and visibility of "Sort by" dropdown
        sort_by_dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-sort-order")))
        self.assertIsNotNone(sort_by_dropdown, "Sort by dropdown is not visible.")

        # Check that the products list is visible
        products_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        self.assertIsNotNone(products_list, "Products list is not visible.")

        # Check cart button
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
        self.assertIsNotNone(cart_button, "Cart button is not visible.")
        
        # Check sign-in link
        sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertIsNotNone(sign_in_link, "Sign in link is not visible.")
        
        # Simulate interactions, e.g., click on the cart
        cart_button.click()
        # Verify UI reaction, such as seeing the cart page or tooltip

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()