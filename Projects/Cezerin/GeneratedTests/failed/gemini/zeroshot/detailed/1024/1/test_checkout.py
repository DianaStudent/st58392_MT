import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://localhost:3000/"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # 1. Open home page.
        self.driver.get(self.base_url)

        # 2. Click on product category.
        category_a_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        category_a_link.click()

        # 3. Select the first product.
        product_a_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
        product_a_link.click()

        # 4. Click the "Add to cart" button.
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not present.")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button.click()

        # 8. Wait for the checkout form to appear.
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))

        # 9. Fill out the checkout form fields.
        email_field.send_keys("mail@mail.com")
        phone_field = self.driver.find_element(By.ID, "customer.mobile")
        phone_field.send_keys("12345678")
        state_field = self.driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = self.driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # 10. Select a shipping method and a payment method.
        shipping_method_radio = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='shipping_method_id']")))
        shipping_method_radio.click()
        payment_method_radio = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='payment_method_id']")))
        payment_method_radio.click()

        # 11. Click the "Next" button.
        next_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
        next_button.click()

        # 12. Click the "Place Order" button.
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
        place_order_button.click()

        # 13. Wait for the confirmation page and check that it includes the text "Thanks for your order!".
        success_message_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        success_message = success_message_element.text
        self.assertIn("Thanks for your order!", success_message, "Confirmation message is not found.")

if __name__ == "__main__":
    unittest.main()