import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MedusaCheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page and click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] img")))
        product_image.click()

        # Step 4: Select a size
        size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='product-options'] button")))
        size_button.click()

        # Step 5: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 6: Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        self.fill_checkout_fields(driver, wait)

        # Step 9: Select delivery and payment methods
        self.select_delivery_and_payment(driver, wait)

        # Step 10: Click "Place Order"
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 11: Verify the confirmation page
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your order was placed successfully')]")))
        self.assertTrue('Your order was placed successfully' in confirmation_message.text, "Order confirmation message not found")

    def fill_checkout_fields(self, driver, wait):
        fields = {
            "shipping-first-name-input": "user",
            "shipping-last-name-input": "test",
            "shipping-address-input": "street 1",
            "shipping-postal-code-input": "LV-1021",
            "shipping-city-input": "Riga",
            "shipping-email-input": "user@test.com"
        }

        for field_id, value in fields.items():
            field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[data-testid='{field_id}']")))
            field.clear()
            field.send_keys(value)

        country_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.send_keys("Denmark" + Keys.ENTER)

        continue_to_delivery_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

    def select_delivery_and_payment(self, driver, wait):
        delivery_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button")))
        delivery_option.click()

        continue_to_payment_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        payment_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:'] button")))
        payment_option.click()

        continue_to_review_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()