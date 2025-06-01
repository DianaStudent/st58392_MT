import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8000/dk')
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        
        # 1. Open home page
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Ecommerce Starter Template']")))
        
        # 2. Click on the menu button
        menu_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()
        
        # 3. Click on the "Store" link
        store_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()
        
        # 4. Click on a product image (thumbnail)
        product_thumbnail = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@data-testid='products-list']//img[@alt='Thumbnail']")))
        product_thumbnail.click()
        
        # 5. Select a size
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 6. Click the "Add to Cart" button
        add_to_cart_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
        if "Out of stock" in add_to_cart_button.text:
            self.fail("Product is out of stock.")
        add_to_cart_button.click()
        
        # 7. Click the cart button to open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()
        
        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # 8. Click "Go to checkout", fill checkout fields
        self.fill_checkout_fields()
        
        # 9. Select delivery and payment methods
        self.select_delivery_and_payment_methods()
        
        # 10. Click "Place Order"
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()
        
        # 11. Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
        self.assertIsNotNone(confirmation_message, "Confirmation message not found.")

    def fill_checkout_fields(self):
        self.fill_input_field("//input[@data-testid='shipping-first-name-input']", "user")
        self.fill_input_field("//input[@data-testid='shipping-last-name-input']", "test")
        self.fill_input_field("//input[@data-testid='shipping-address-input']", "street 1")
        self.fill_input_field("//input[@data-testid='shipping-postal-code-input']", "LV-1021")
        self.fill_input_field("//input[@data-testid='shipping-city-input']", "Riga")
        
        country_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-testid='shipping-country-select']")))
        country_select.click()
        country_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Denmark']")))
        country_option.click()

        self.fill_input_field("//input[@data-testid='shipping-email-input']", "user@test.com")

        submit_address_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']")))
        submit_address_button.click()

    def fill_input_field(self, xpath, text):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        if not element:
            self.fail(f"Element with XPath '{xpath}' not found.")
        element.clear()
        element.send_keys(text)

    def select_delivery_and_payment_methods(self):
        delivery_option_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Express Shipping']/preceding-sibling::div/button")))
        delivery_option_button.click()

        continue_to_payment_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        payment_option_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Manual Payment']/preceding-sibling::div/button")))
        payment_option_button.click()

        continue_to_review_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']")))
        continue_to_review_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()