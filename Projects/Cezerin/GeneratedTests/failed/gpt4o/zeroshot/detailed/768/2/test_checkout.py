from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open home page (already done in setUp)

        # Step 2: Click on product category
        category_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product
        product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'button') and text()='GO TO CHECKOUT']")))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_field = self.wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form fields
        email_field.send_keys("mail@mail.com")
        phone_field = driver.find_element(By.ID, "customer.mobile")
        phone_field.send_keys("12345678")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        shipping_method.click()
        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        payment_method.click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check for the success message
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertTrue(success_message.is_displayed(), "Success message is not displayed")

if __name__ == "__main__":
    unittest.main()