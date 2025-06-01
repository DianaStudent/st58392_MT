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

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Open home page
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # Click the menu button
            menu_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='nav-menu-button']")))
            menu_button.click()

            # Click the "Store" link
            store_link = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-testid='store-link']")))
            store_link.click()

            # Click on a product image (Thumbnail) - first product
            product_image = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//ul[@data-testid='products-list']//li[1]//img")))
            product_image.click()

            # Select size by clicking the size button "L"
            size_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
            size_button.click()

            # Add the product to the cart
            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='add-product-button']")))
            add_to_cart_button.click()

            # Click the cart button to open the cart
            cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-testid='nav-cart-link']")))
            cart_button.click()

            # Wait for "Go to cart" button
            go_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='go-to-cart-button']")))
            go_to_cart_button.click()

            # Fill checkout fields
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))).send_keys("user")
            driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']").send_keys("test")
            driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']").send_keys("street 1")
            driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']").send_keys("LV-1021")
            driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']").send_keys("Riga")
            country_select = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//select[@data-testid='shipping-country-select']")))
            country_select.click()
            country_select.find_element(By.XPATH, "//option[@value='dk']").click()
            driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']").send_keys("user@test.com")

            # Click "Continue to delivery"
            continue_to_delivery = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='submit-address-button']")))
            continue_to_delivery.click()

            # Select delivery method - radio button
            delivery_radio = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//span[@data-testid='delivery-option-radio'])[1]")))
            delivery_radio.click()

            # Click "Continue to payment"
            continue_to_payment = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
            continue_to_payment.click()

            # Select payment method - radio button
            payment_radio = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//span[@data-testid='radio-button'])[1]")))
            payment_radio.click()

            # Click "Continue to review"
            continue_to_review = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='submit-payment-button']")))
            continue_to_review.click()

            # Click "Place Order"
            place_order_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='submit-order-button']")))
            place_order_button.click()

            # Verify the confirmation page
            confirmation_text = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[@data-testid='order-complete-container']//span[text()='Your order was placed successfully.']")))

            self.assertTrue(confirmation_text.is_displayed())

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()