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

        # Open home page and wait for Category A link
        category_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Select the first product
        product_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Add product to the cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.button-addtocart button.button")))
        add_to_cart_button.click()

        # Open the shopping cart
        cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Verify presence of "GO TO CHECKOUT" button
        go_to_checkout_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered"))
        )
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present in the cart.")

        # Proceed to checkout
        go_to_checkout_button.click()

        # Wait for the checkout form
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#customer\\.email")))

        # Fill checkout form fields
        driver.find_element(By.CSS_SELECTOR, "input#customer\\.email").send_keys("mail@mail.com")
        driver.find_element(By.CSS_SELECTOR, "input#customer\\.mobile").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, "input#shipping_address\\.state").send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, "input#shipping_address\\.city").send_keys("Riga")

        # Select a shipping method and a payment method
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='shipping_method_id']"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='payment_method_id']"))).click()

        # Click "Next"
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.button.is-primary")
        next_button.click()

        # Place the order
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.button.is-primary"))
        )
        place_order_button.click()

        # Verify order confirmation
        thank_you_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.checkout-success-title"))
        )
        if "Thanks for your order!" not in thank_you_message.text:
            self.fail("Order success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()