import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartAndCheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_and_checkout(self):
        # 1. Open home page.

        # 2. Click on product category.
        category_a_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        if not category_a_link:
            self.fail("Category A link not found")
        category_a_link.click()

        # 3. Select the first product.
        product_a_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
        if not product_a_link:
            self.fail("Product A link not found")
        product_a_link.click()

        # 4. Click the "Add to cart" button.
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        if not cart_button:
            self.fail("Cart button not found")
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        if not go_to_checkout_button.is_displayed():
            self.fail("GO TO CHECKOUT button is not present.")
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not present.")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button.click()

        # 8. Wait for the checkout form to appear.
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))

        # 9. Fill out the checkout form fields.
        email_field.send_keys("mail@mail.com")
        mobile_field = self.driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")
        state_field = self.driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = self.driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # 10. Select a shipping method and a payment method.
        shipping_method_radio = self.wait.until(EC.element_to_be_clickable((By.NAME, "shipping_method_id")))
        shipping_method_radio.click()
        payment_method_radio = self.wait.until(EC.element_to_be_clickable((By.NAME, "payment_method_id")))
        payment_method_radio.click()

        # 11. Click the "Next" button.
        next_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
        next_button.click()

        # 12. Click the "Place Order" button.
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
        place_order_button.click()

        # 13. Wait for the confirmation page and check that it includes the text "Thanks for your order!".
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        if not success_message:
            self.fail("Success message not found")
        self.assertTrue("Thanks for your order!" in success_message.text, "Confirmation message is not present.")

if __name__ == "__main__":
    unittest.main()