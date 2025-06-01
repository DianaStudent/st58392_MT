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
        wait = self.wait

        # Click the menu button ("Menu").
        menu_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # Click the "Store" link.
        store_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Click on a product image (Thumbnail) - first product.
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, "(//ul[@data-testid='products-list']/li//img)[1]")))
        first_product.click()

        # Select size by clicking the size button "L".
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Add the product to the cart.
        add_product_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button']")))
        add_product_button.click()

        # Wait for the cart to show item count "1" and click the cart button (shopping bag).
        nav_cart_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link' and contains(text(), 'Cart (1)')]")))
        nav_cart_link.click()

        # Click "Go to checkout".
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields.
        first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']")))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']")
        last_name_input.send_keys("test")

        address_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']")
        address_input.send_keys("street 1")

        postal_code_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']")
        postal_code_input.send_keys("LV-1021")

        city_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']")
        city_input.send_keys("Riga")

        country_select = driver.find_element(By.XPATH, "//select[@data-testid='shipping-country-select']")
        country_select.send_keys("Denmark")

        email_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']")
        email_input.send_keys("user@test.com")

        # Click "Continue to delivery".
        submit_address_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
        submit_address_button.click()

        # Select delivery method - radio button.
        delivery_radio_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@data-testid='radio-button'])[1]")))
        delivery_radio_button.click()

        # Click "Continue to payment".
        continue_to_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment method - radio button.
        payment_radio_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@data-testid='radio-button'])[1]")))
        payment_radio_button.click()

        # Click "Continue to review".
        continue_to_review_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Click "Place Order".
        place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify the confirmation page contains: "Your order was placed successfully".
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']//span[text()='Your order was placed successfully.']")))
        self.assertTrue(confirmation_message, "Order confirmation message was not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()