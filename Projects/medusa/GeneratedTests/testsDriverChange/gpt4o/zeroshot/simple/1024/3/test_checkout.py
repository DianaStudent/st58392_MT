import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout(self):
        driver = self.driver
        wait = self.wait

        # Open the menu and navigate to the Store page
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()
        
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Select a product
        product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a")))
        product.click()

        # Select size and add to cart
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart.click()

        # Go to cart
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_link.click()

        go_to_checkout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill required checkout fields
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']").send_keys("Denmark")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

        submit_address_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
        submit_address_button.click()

        # Select delivery option
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']")))
        delivery_option.click()

        submit_delivery_option = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        submit_delivery_option.click()

        # Select payment method
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:']")))
        payment_option.click()

        submit_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        submit_payment_button.click()

        # Place the order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Confirm the order success
        order_success_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']"))
        )
        if not order_success_text:
            self.fail("Order success message is not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()