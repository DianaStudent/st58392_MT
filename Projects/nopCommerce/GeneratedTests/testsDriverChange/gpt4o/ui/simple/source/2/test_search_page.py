import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestStoreUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-logo img')))
            self.assertIsNotNone(logo, "Logo is not visible")

            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            self.assertIsNotNone(search_box, "Search box is not visible")

            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-1.search-box-button')))
            self.assertIsNotNone(search_button, "Search button is not visible")

            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-register')))
            self.assertIsNotNone(register_link, "Register link is not visible")

            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-login')))
            self.assertIsNotNone(login_link, "Login link is not visible")

            wishlist = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-wishlist')))
            self.assertIsNotNone(wishlist, "Wishlist link is not visible")

            cart = wait.until(EC.visibility_of_element_located((By.ID, 'topcartlink')))
            self.assertIsNotNone(cart, "Cart link is not visible")
        
        except Exception as e:
            self.fail(f"Failed to locate elements in the header: {str(e)}")
        
        # Check that search form elements are present and visible
        try:
            search_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-title h1')))
            self.assertIsNotNone(search_title, "Search title is not visible")

            advanced_search_checkbox = driver.find_element(By.ID, 'advs')
            self.assertTrue(advanced_search_checkbox.is_displayed(), "Advanced search checkbox is not visible")
        
        except Exception as e:
            self.fail(f"Failed to locate search form elements: {str(e)}")
        
        # Check products and buttons in the product grid
        try:
            product_grid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-grid')))
            self.assertIsNotNone(product_grid, "Product grid is not visible")

            add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, '.button-2.product-box-add-to-cart-button')
            self.assertTrue(all(button.is_displayed() for button in add_to_cart_buttons), "Not all 'Add to cart' buttons are visible")

        except Exception as e:
            self.fail(f"Failed to locate product grid elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()