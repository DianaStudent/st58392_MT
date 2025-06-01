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

        # 1. Click on product category.
        category_a_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
        )
        category_a_link.click()

        # 2. Select the first product.
        product_a_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
        )
        product_a_link.click()

        # 3. Click the "Add to cart" button.
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
        )
        add_to_cart_button.click()

        # 4. Click the cart icon/button to open the shopping bag.
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        cart_button.click()

        # 5. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
        )
        self.assertTrue(go_to_checkout_button.is_displayed())

        # 6. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button.click()

        # 7. Fill required checkout fields
        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        email_field.send_keys("mail@mail.com")

        mobile_field = wait.until(
            EC.presence_of_element_located((By.ID, "customer.mobile"))
        )
        mobile_field.send_keys("12345678")

        state_field = wait.until(
            EC.presence_of_element_located((By.ID, "shipping_address.state"))
        )
        state_field.send_keys("Riga")

        city_field = wait.until(
            EC.presence_of_element_located((By.ID, "shipping_address.city"))
        )
        city_field.send_keys("Riga")

        # 8. Select a shipping and payment method.
        shipping_method = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='shipping_method_id']"))
        )
        shipping_method.click()

        payment_method = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='payment_method_id']"))
        )
        payment_method.click()

        # 9. Click "Next"
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
        )
        next_button.click()

        # 10. Click "Place Order" to complete the process.
        place_order_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
        )
        place_order_button.click()

        # 11. Confirm that the success page contains the message: "Thanks for your order!".
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )

        if success_message and success_message.text:
            self.assertIn("Thanks for your order!", success_message.text)
        else:
            self.fail("Success message not found or is empty.")

if __name__ == "__main__":
    unittest.main()