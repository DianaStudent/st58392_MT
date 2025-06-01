import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Open home page and verify
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Click the menu button ("Menu")
        menu_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # Click the "Store" link
        store_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Click on the first product image (Thumbnail)
        product_thumbnail = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-testid='product-wrapper']/div/img)[1]")))
        product_thumbnail.click()

        # Select size by clicking the size button "L"
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='option-button' and text()='L'])[1]")))
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Explicitly click the cart button
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Click "Go to checkout"
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))).send_keys("user")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-last-name-input']"))).send_keys("test")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-address-input']"))).send_keys("street 1")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-postal-code-input']"))).send_keys("LV-1021")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-city-input']"))).send_keys("Riga")

        country_select = self.wait.until(EC.presence_of_element_located((By.XPATH, "//select[@data-testid='shipping-country-select']")))
        country_select.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='dk']"))).click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-email-input']"))).send_keys("user@test.com")

        # Click "Continue to delivery"
        continue_to_delivery_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # Select delivery method
        delivery_method = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@data-testid='delivery-option-radio']//button[@data-testid='radio-button'])[1]")))
        delivery_method.click()

        # Click "Continue to payment"
        continue_to_payment_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Select payment method
        payment_method = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button'])[1]")))
        payment_method.click()

        # Click "Continue to review"
        continue_to_review_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Click "Place Order"
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify the confirmation page
        order_confirmation_text = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
        
        if not order_confirmation_text:
            self.fail("Order confirmation text was not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()