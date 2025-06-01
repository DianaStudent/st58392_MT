from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 2: Click on product category "Category A"
        category_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product "Product A"
        product_a_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Step 6: Verify the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT")))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button not displayed in cart.")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_field = self.wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form fields
        email_field.send_keys("mail@mail.com")
        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        shipping_method.click()
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        payment_method.click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.button.is-primary")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check "Thanks for your order!" text
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertTrue("Thanks for your order!" in success_message.text, "Order confirmation message not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()