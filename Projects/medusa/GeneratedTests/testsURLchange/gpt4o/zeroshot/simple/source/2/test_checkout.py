import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestMedusaStoreCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8000/dk")
    
    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the store page
        store_link = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "nav-store-link")))
        store_link.click()

        # Click on the product
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Medusa Sweatshirt']/ancestor::a")))
        product_link.click()

        # Select size
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Add to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "add-product-button")))
        add_to_cart_button.click()

        # Go to cart
        cart_link = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "nav-cart-link")))
        cart_link.click()

        # Proceed to checkout
        checkout_button = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "go-to-checkout-button")))
        checkout_button.click()

        # Fill shipping details
        wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "shipping-first-name-input"))).send_keys("user")
        driver.find_element(By.DATA_TEST_ID, "shipping-last-name-input").send_keys("test")
        driver.find_element(By.DATA_TEST_ID, "shipping-address-input").send_keys("street 1")
        driver.find_element(By.DATA_TEST_ID, "shipping-postal-code-input").send_keys("LV-1021")
        driver.find_element(By.DATA_TEST_ID, "shipping-city-input").send_keys("Riga")
        country_select = driver.find_element(By.DATA_TEST_ID, "shipping-country-select")
        country_select.send_keys("Denmark")
        driver.find_element(By.DATA_TEST_ID, "shipping-email-input").send_keys("user@test.com")

        # Continue to delivery
        continue_to_delivery_button = driver.find_element(By.DATA_TEST_ID, "submit-address-button")
        continue_to_delivery_button.click()

        # Select delivery option
        delivery_option_radio = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "delivery-option-radio")))
        delivery_option_radio.click()
        continue_to_payment_button = driver.find_element(By.DATA_TEST_ID, "submit-delivery-option-button")
        continue_to_payment_button.click()

        # Select payment method
        payment_radio_button = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Manual Payment']")))
        payment_radio_button.click()
        continue_to_review_button = driver.find_element(By.DATA_TEST_ID, "submit-payment-button")
        continue_to_review_button.click()

        # Place order
        place_order_button = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "submit-order-button")))
        place_order_button.click()

        # Verify order success
        order_success_text = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']")))
        if "Your order was placed successfully." not in order_success_text.text:
            self.fail("Order success message not found!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()