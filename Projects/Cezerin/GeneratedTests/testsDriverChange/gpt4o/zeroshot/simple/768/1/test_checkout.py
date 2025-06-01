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
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to "Category A"
        category_a_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
        category_a_link.click()

        # Open "Product A"
        product_a_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
        product_a_link.click()

        # Add to cart
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_btn.click()

        # Go to checkout
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Wait for "GO TO CHECKOUT" button
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT")))
        go_to_checkout_button.click()

        # Fill in checkout details
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        mobile_field = driver.find_element(By.ID, "customer.mobile")
        country_field = driver.find_element(By.ID, "shipping_address.country")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        city_field = driver.find_element(By.ID, "shipping_address.city")
        payment_method_radio = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id'][value='67ca982ef38a654a7c2c1a6a']")
        shipping_method_radio = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id'][value='67ca982ef38a654a7c2c1a69']")

        email_field.send_keys("mail@mail.com")
        mobile_field.send_keys("12345678")
        country_field.clear()
        country_field.send_keys("SG")
        state_field.send_keys("Riga")
        city_field.send_keys("Riga")
        payment_method_radio.click()
        shipping_method_radio.click()

        # Submit the checkout form
        next_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button.button.is-primary")
        next_button.click()

        # Finalizing order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.is-primary")))
        place_order_button.click()

        # Confirm success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()