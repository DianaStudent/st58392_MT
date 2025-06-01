import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page. (Done in setUp)

        # 2. Click on product category.
        category_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        if category_a_link:
            category_a_link.click()
        else:
            self.fail("Category A link not found")

        # 3. Select the first product.
        product_a_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        if product_a_link:
            product_a_link.click()
        else:
            self.fail("Product A link not found")

        # 4. Click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found")

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        if go_to_checkout_button:
            self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not present.")
        else:
            self.fail("GO TO CHECKOUT button is not present in the cart")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout")))
        if go_to_checkout_button:
            go_to_checkout_button.click()
        else:
            self.fail("GO TO CHECKOUT button is not clickable")

        # 8. Fill required checkout fields
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        if email_field:
            email_field.send_keys("mail@mail.com")
        else:
            self.fail("Email field not found")

        mobile_field = wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        if mobile_field:
            mobile_field.send_keys("12345678")
        else:
            self.fail("Mobile field not found")

        state_field = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        if state_field:
            state_field.send_keys("Riga")
        else:
            self.fail("State field not found")

        city_field = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        if city_field:
            city_field.send_keys("Riga")
        else:
            self.fail("City field not found")

        # 9. Select a shipping and payment method.
        shipping_method = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='shipping_method_id']")))
        if shipping_method:
            shipping_method.click()
        else:
            self.fail("Shipping method not found")

        payment_method = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='payment_method_id']")))
        if payment_method:
            payment_method.click()
        else:
            self.fail("Payment method not found")

        # 10. Click "Next" and then "Place Order" to complete the process.
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
        if next_button:
            next_button.click()
        else:
            self.fail("Next button not found")

        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        if place_order_button:
            place_order_button.click()
        else:
            self.fail("Place order button not found")

        # 11. Confirm that the success page contains the message: "Thanks for your order!".
        success_message_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='checkout-success-title']")))
        if success_message_element:
            success_message = success_message_element.text
            self.assertIn("Thanks for your order!", success_message, "Success message is not found.")
        else:
            self.fail("Success message element not found")


if __name__ == "__main__":
    unittest.main()