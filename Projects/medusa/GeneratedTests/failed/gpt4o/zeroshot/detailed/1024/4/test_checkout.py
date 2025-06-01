from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Open home page and click the menu button ("Menu").
        menu_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # 2. Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # 3. Click on the first product image (Thumbnail).
        first_product_thumbnail = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//div[@data-testid='product-wrapper']//img)[1]")))
        first_product_thumbnail.click()

        # 4. Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 5. Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # 6. Click the cart button.
        cart_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Wait for "Go to checkout" button
        go_to_checkout_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # 7. Fill out the checkout fields
        required_fields = {
            "shipping-first-name-input": "user",
            "shipping-last-name-input": "test",
            "shipping-address-input": "street 1",
            "shipping-postal-code-input": "LV-1021",
            "shipping-city-input": "Riga",
            "shipping-email-input": "user@test.com"
        }

        for test_id, value in required_fields.items():
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//input[@data-testid='{test_id}']")))
            element.clear()
            element.send_keys(value)

        # Select country
        country_select = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select[@data-testid='shipping-country-select']")))
        country_select.click()
        country_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//option[@value='dk']")))
        country_option.click()

        # 8. Click "Continue to delivery"
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # 9. Select delivery method - radio button
        delivery_method_radio = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@data-testid='delivery-option-radio']//button[@data-testid='radio-button'])[1]")))
        delivery_method_radio.click()

        # 10. Click "Continue to payment"
        continue_to_payment_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # 11. Select payment method - radio button
        payment_method_radio = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button'])")))
        payment_method_radio.click()

        # 12. Click "Continue to review"
        continue_to_review_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # 13. Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # 14. Verify the confirmation page
        confirmation_message = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h1/span[contains(text(), 'Your order was placed successfully.')]")))
        self.assertTrue(confirmation_message.is_displayed(), "Confirmation message not found or hidden.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()