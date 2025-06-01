import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.url = "http://localhost:8000/dk"

    def test_checkout_process(self):
        driver, wait = self.driver, self.wait
        driver.get(self.url)
        
        # Step 1: Click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a img")))
        product_image.click()

        # Step 4: Select a size
        size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        # Step 5: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 6: Click the cart button to open the cart
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_link.click()

        # Step 7: Click "Go to checkout" button
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Step 8: Fill the checkout fields
        self.fill_checkout_form()

        # Step 9: Select delivery and payment methods
        submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        submit_delivery_option_button.click()
        
        # Select manual payment
        submit_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        submit_payment_button.click()

        # Step 10: Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 11: Verify the confirmation page
        confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Your order was placed successfully')]")))
        self.assertIsNotNone(confirmation_text)

    def fill_checkout_form(self):
        # Fill out checkout form details
        self.fill_element("input[data-testid='shipping-first-name-input']", "user")
        self.fill_element("input[data-testid='shipping-last-name-input']", "test")
        self.fill_element("input[data-testid='shipping-address-input']", "street 1")
        self.fill_element("input[data-testid='shipping-postal-code-input']", "LV-1021")
        self.fill_element("input[data-testid='shipping-city-input']", "Riga")
        
        # Select country
        country_select = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.click()
        country_option = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[data-testid='shipping-country-select'] option[value='dk']")))
        country_option.click()

        # Fill out email
        self.fill_element("input[data-testid='shipping-email-input']", "user@test.com")

        # Continue to delivery
        continue_to_delivery_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

    def fill_element(self, selector, value):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        element.clear()
        element.send_keys(value)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()