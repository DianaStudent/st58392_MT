import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the menu button
        try:
            menu_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='nav-menu-button']")))
            menu_button.click()
        except:
            self.fail("Menu button not found!")

        # Step 2: Click the "Store" link
        try:
            store_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='store-link']")))
            store_link.click()
        except:
            self.fail("Store link not found!")

        # Step 3: Click on the first product image
        try:
            product_image = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@data-testid='products-list']//img[@alt='Thumbnail']")))
            product_image.click()
        except:
            self.fail("Product image not found!")

        # Step 4: Select size "L"
        try:
            size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button'][text()='L']")))
            size_button.click()
        except:
            self.fail("Size L button not found!")

        # Step 5: Add the product to the cart
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found!")

        # Step 6: Explicitly click the cart button
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
            cart_button.click()
        except:
            self.fail("Cart button not found!")

        # Step 7: Click "Go to checkout"
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-checkout-button']")))
            go_to_checkout_button.click()
        except:
            self.fail("Go to checkout button not found!")

        # Step 8: Fill checkout fields
        self.fill_checkout_fields()

        # Step 9: Click "Continue to delivery"
        try:
            continue_to_delivery_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-address-button']")))
            continue_to_delivery_button.click()
        except:
            self.fail("Continue to delivery button not found!")

        # Step 10: Select delivery method
        try:
            delivery_option_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='delivery-option-radio']//button")))
            delivery_option_radio.click()
        except:
            self.fail("Delivery option radio button not found!")

        # Step 11: Click "Continue to payment"
        try:
            continue_to_payment_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
            continue_to_payment_button.click()
        except:
            self.fail("Continue to payment button not found!")

        # Step 12: Select payment method
        try:
            payment_method_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='headlessui-radiogroup-:rj:']//button")))
            payment_method_radio.click()
        except:
            self.fail("Payment method radio button not found!")

        # Step 13: Click "Continue to review"
        try:
            continue_to_review_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-payment-button']")))
            continue_to_review_button.click()
        except:
            self.fail("Continue to review button not found!")

        # Step 14: Click "Place order"
        try:
            place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-order-button']")))
            place_order_button.click()
        except:
            self.fail("Place order button not found!")

        # Step 15: Verify order confirmation
        try:
            confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Your order was placed successfully.')]")))
            self.assertIsNotNone(confirmation_message, "Order confirmation message not found!")
        except:
            self.fail("Order confirmation message not detected!")

    def fill_checkout_fields(self):
        wait = self.wait
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))).send_keys("user")
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-last-name-input']"))).send_keys("test")
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-address-input']"))).send_keys("street 1")
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-postal-code-input']"))).send_keys("LV-1021")
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-city-input']"))).send_keys("Riga")

            country_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@data-testid='shipping-country-select']")))
            country_select.click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//select[@data-testid='shipping-country-select']/option[@value='dk']"))).click()

            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-email-input']"))).send_keys("user@test.com")
        except:
            self.fail("Error filling checkout fields!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()