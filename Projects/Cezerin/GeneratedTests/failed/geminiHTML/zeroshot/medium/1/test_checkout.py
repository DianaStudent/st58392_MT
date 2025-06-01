import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartCheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_checkout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page. (Done in setUp)

        # 2. Click on product category "Category A".
        category_a_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
        if category_a_link:
            category_a_link.click()
        else:
            self.fail("Category A link not found.")

        # 3. Select the first product "Product A".
        product_a_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
        if product_a_link:
            product_a_link.click()
        else:
            self.fail("Product A link not found.")

        # 4. Click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found.")

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found in the cart.")

        # 7. Click the "GO TO CHECKOUT" button.
        if go_to_checkout_button:
            go_to_checkout_button.click()
        else:
            self.fail("GO TO CHECKOUT button not found.")

        # 8. Fill required checkout fields
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        mobile_field = wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        state_field = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        city_field = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))

        if email_field and mobile_field and state_field and city_field:
            email_field.send_keys("mail@mail.com")
            mobile_field.send_keys("12345678")
            state_field.send_keys("Riga")
            city_field.send_keys("Riga")
        else:
            self.fail("One or more checkout fields not found.")

        # 9. Select a shipping and payment method.
        shipping_method = wait.until(EC.presence_of_element_located((By.NAME, "shipping_method_id")))
        payment_method = wait.until(EC.presence_of_element_located((By.NAME, "payment_method_id")))

        if shipping_method and payment_method:
            driver.find_element(By.XPATH, "//input[@name='shipping_method_id']").click()
            driver.find_element(By.XPATH, "//input[@name='payment_method_id']").click()
        else:
            self.fail("Shipping or payment method not found.")

        # 10. Click "Next" and then "Place Order" to complete the process.
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
        if next_button:
            next_button.click()
        else:
            self.fail("Next button not found.")

        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
        if place_order_button:
            place_order_button.click()
        else:
            self.fail("Place Order button not found.")

        # 11. Confirm that the success page contains the message: "Thanks for your order!".
        success_message_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        if success_message_element:
            success_message = success_message_element.text
            self.assertIn("Thanks for your order!", success_message, "Success message not found on the final page.")
        else:
            self.fail("Success message element not found.")

if __name__ == "__main__":
    unittest.main()