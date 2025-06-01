from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page (already done in setUp)

        # 2. Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (thumbnail)
        product_wrapper = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
        product_wrapper.click()

        # 5. Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button'][text()='L']")))
        size_button.click()

        # 6. Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # 7. Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']")))
        cart_button.click()

        # 8. Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # 9. Fill checkout fields
        shipping_first_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
        shipping_first_name_input.clear()
        shipping_first_name_input.send_keys("user")

        shipping_last_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")))
        shipping_last_name_input.clear()
        shipping_last_name_input.send_keys("test")

        shipping_address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")))
        shipping_address_input.clear()
        shipping_address_input.send_keys("street 1")

        shipping_postal_code_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")))
        shipping_postal_code_input.clear()
        shipping_postal_code_input.send_keys("LV-1021")

        shipping_city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")))
        shipping_city_input.clear()
        shipping_city_input.send_keys("Riga")

        shipping_country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        shipping_country_select.click()
        country_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select'] option[value='dk']")))
        country_option.click()

        shipping_email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")))
        shipping_email_input.clear()
        shipping_email_input.send_keys("user@test.com")

        submit_address_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        submit_address_button.click()

        # Select delivery method
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']:first-child button[data-testid='radio-button']")))
        delivery_option.click()

        submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        submit_delivery_option_button.click()

        # Select payment method
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']")))
        payment_option.click()

        submit_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        submit_payment_button.click()

        # 10. Click "Place Order"
        submit_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        submit_order_button.click()

        # 11. Verify the confirmation page contains: "Your order was placed successfully"
        order_complete_text_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]")))
        if order_complete_text_element:
            order_complete_text = order_complete_text_element.text
            self.assertEqual(order_complete_text, "Your order was placed successfully.")
        else:
            self.fail("Order complete text not found")

if __name__ == "__main__":
    unittest.main()