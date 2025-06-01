import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class MedusaCheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "http://localhost:8000/dk"
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page - already done in setUp

        # 2. Click the menu button ("Menu").
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (Thumbnail) - first product.
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
        product_link.click()

        # 5. Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
        size_button.click()

        # 6. Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        
        # Check if the button is "Out of stock"
        if add_to_cart_button.text == "Out of stock":
            self.fail("Product is out of stock, cannot add to cart.")
        
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']")))
        cart_button.click()
        
        # 8. Click "Go to cart"
        go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']")))
        go_to_cart_button.click()

        # 9. Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
        go_to_checkout_button.click()

        # Fill checkout fields:
        # - First name: user
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
        first_name_input.clear()
        first_name_input.send_keys("user")

        # - Last name: test
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")))
        last_name_input.clear()
        last_name_input.send_keys("test")

        # - Address: street 1
        address_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")))
        address_input.clear()
        address_input.send_keys("street 1")

        # - Postal code: LV-1021
        postal_code_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")))
        postal_code_input.clear()
        postal_code_input.send_keys("LV-1021")

        # - City: Riga
        city_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")))
        city_input.clear()
        city_input.send_keys("Riga")

        # - Country: Denmark - combo box
        country_select = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))))
        country_select.select_by_value("dk")

        # - Email: user@test.com
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")))
        email_input.clear()
        email_input.send_keys("user@test.com")

        # 10. Click "Continue to delivery"
        submit_address_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        submit_address_button.click()

        # 11. Select delivery method - radio button
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button[data-testid='radio-button']")))
        delivery_option.click()

        # 12. Click "Continue to payment"
        submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        submit_delivery_option_button.click()

        # 13. Select payment method - radio button
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id*='headlessui-radio-'] button[data-testid='radio-button']")))
        payment_option.click()

        # 14. Click "Continue to review"
        submit_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        submit_payment_button.click()

        # 15. Click "Place Order".
        submit_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        submit_order_button.click()

        # 16. Verify the confirmation page contains: "Your order was placed successfully".
        order_complete_text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]"))).text
        self.assertEqual(order_complete_text, "Your order was placed successfully.")

if __name__ == "__main__":
    unittest.main()