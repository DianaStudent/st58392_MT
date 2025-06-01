from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Open home page.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logo-image")))

        # 2. Click on product category.
        category_a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a.click()

        # 3. Select the first product.
        product_a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a.click()

        # 4. Click the "Add to cart" button.
        add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary")))
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is missing")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button.click()

        # 8. Wait for the checkout form to appear and fill it.
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        phone_field = driver.find_element(By.ID, "customer.mobile")
        phone_field.send_keys("12345678")

        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # 10. Select a shipping method and a payment method.
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        shipping_method.click()

        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        payment_method.click()

        # 11. Click the "Next" button.
        next_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap .checkout-button")
        next_button.click()

        # 12. Click the "Place Order" button.
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-step .checkout-button.is-primary")))
        place_order_button.click()

        # 13. Wait for the confirmation page and check that it includes the text "Thanks for your order!".
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        self.assertIn("Thanks for your order!", success_message.text, "Order success message is missing or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()