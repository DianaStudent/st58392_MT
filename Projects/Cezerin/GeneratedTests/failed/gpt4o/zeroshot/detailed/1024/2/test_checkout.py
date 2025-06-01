import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open home page and click on the category
        category_a = self.wait.until(element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # Step 2: Select the first product
        product_a = self.wait.until(element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # Step 3: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 4: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Step 5: Verify presence of "GO TO CHECKOUT" button
        go_to_checkout_button = self.wait.until(element_to_be_clickable((By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]")))
        self.assertIsNotNone(go_to_checkout_button)

        # Step 6: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 7: Wait for the checkout form to appear
        email_field = self.wait.until(element_to_be_clickable((By.ID, "customer.email")))

        # Step 8: Fill out the checkout form fields
        email_field.send_keys("mail@mail.com")
        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Step 9: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        shipping_method.click()
        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        payment_method.click()

        # Step 10: Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.button.is-primary")
        next_button.click()

        # Step 11: Click the "Place Order" button
        place_order_button = self.wait.until(element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.button.is-primary")))
        place_order_button.click()

        # Step 12: Wait for the confirmation page and check for order confirmation text
        confirmation_text = self.wait.until(text_to_be_present_in_element((By.CSS_SELECTOR, "h1.checkout-success-title"), "Thanks for your order!"))
        self.assertTrue(confirmation_text, "Order confirmation text not found!")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()