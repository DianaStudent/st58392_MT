import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Open home page
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))

        # Click on product category
        category_link = driver.find_element(By.CSS_SELECTOR, "a[href='/category-a']")
        category_link.click()

        # Select the first product
        product_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button-addtocart button.button")))
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered")))
        if not go_to_checkout_button or go_to_checkout_button.text.strip() != "GO TO CHECKOUT":
            self.fail("GO TO CHECKOUT button is not present in the cart.")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Wait for the checkout form to appear
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#customer\\.email")))

        # Fill out the checkout form fields
        email_field = driver.find_element(By.CSS_SELECTOR, "input#customer\\.email")
        mobile_field = driver.find_element(By.CSS_SELECTOR, "input#customer\\.mobile")
        country_field = driver.find_element(By.CSS_SELECTOR, "input#shipping_address\\.country")
        state_field = driver.find_element(By.CSS_SELECTOR, "input#shipping_address\\.state")
        city_field = driver.find_element(By.CSS_SELECTOR, "input#shipping_address\\.city")

        email_field.send_keys("mail@mail.com")
        mobile_field.send_keys("12345678")
        country_field.clear()
        country_field.send_keys("SG")
        state_field.send_keys("Riga")
        city_field.send_keys("Riga")

        # Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")

        shipping_method.click()
        payment_method.click()

        # Click "Next"
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.button.is-primary")
        next_button.click()

        # Click "Place Order"
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.button.is-primary")))
        place_order_button.click()

        # Verify confirmation page
        thank_you_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.checkout-success-title")))
        if "Thanks for your order!" not in thank_you_message.text:
            self.fail("Order success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()