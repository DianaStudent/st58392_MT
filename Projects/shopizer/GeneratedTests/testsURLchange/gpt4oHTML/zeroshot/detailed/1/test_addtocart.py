import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get('http://localhost/')  # Adjust the base URL as needed

        # Step 1: Open the home page
        try:
            # Check for main product area, validate it's not empty
            product_area = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-area')))
            self.assertTrue(product_area.is_displayed(), "Product area is not displayed or missing.")
        except Exception as e:
            self.fail(f"Home page elements not properly loaded: {e}")

        # Step 2: Hover over the first product
        first_product = driver.find_element(By.CSS_SELECTOR, '.product-wrap-2:first-child .product-img')
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Step 3: Click the revealed "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-wrap-2:first-child .product-action-2 .fa-shopping-cart'))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not clickable: {e}")

        # Step 4: Click the cart icon to open the popup cart
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.icon-cart')))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon not clickable: {e}")

        # Step 5: Wait for the popup to become visible
        try:
            popup_cart = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.shopping-cart-content'))
            )
            self.assertTrue(popup_cart.is_displayed(), "Popup cart is not displayed.")
        except Exception as e:
            self.fail(f"Popup cart not visible: {e}")

        # Step 6: Click "View cart" or similar button inside the popup
        try:
            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.shopping-cart-btn a[href="/cart"]'))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"View cart button not clickable: {e}")

        # Step 7: On the cart page, verify that the product appears in the cart list
        try:
            cart_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-main-area')))
            self.assertTrue(cart_page.is_displayed(), "Cart page is not displayed.")
            
            product_names = driver.find_elements(By.CSS_SELECTOR, '.product-name a')
            product_names_text = [product.text for product in product_names if product.text.strip()]
            self.assertIn("Olive Table", product_names_text, "Product not found in cart.")
        except Exception as e:
            self.fail(f"Product verification in cart failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()