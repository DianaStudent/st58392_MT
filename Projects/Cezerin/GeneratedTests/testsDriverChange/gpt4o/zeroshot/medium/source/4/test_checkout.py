import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "http://localhost:3000/"
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        driver.get(self.url)

        # Step 2: Click on product category
        category_a_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
        )
        category_a_link.click()

        # Step 3: Select the first product
        product_a_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        product_a_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']"))
        )
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Go to checkout']"))
        )
        if go_to_checkout_button is None or not go_to_checkout_button.is_displayed():
            self.fail("Go to checkout button is not present inside the cart")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Fill required checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, 'customer.email')))
        phone_input = wait.until(EC.presence_of_element_located((By.ID, 'customer.mobile')))
        state_input = wait.until(EC.presence_of_element_located((By.ID, 'shipping_address.state')))
        city_input = wait.until(EC.presence_of_element_located((By.ID, 'shipping_address.city')))

        email_input.send_keys("mail@mail.com")
        phone_input.send_keys("12345678")
        state_input.send_keys("Riga")
        city_input.send_keys("Riga")

        # Step 9: Select a shipping and payment method
        shipping_method = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='shipping_method_id']"))
        )
        payment_method = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='payment_method_id']"))
        )
        shipping_method.click()
        payment_method.click()

        # Step 10: Click "Next" and then "Place Order" to complete the process
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
        )
        next_button.click()

        place_order_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
        )
        place_order_button.click()

        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        if success_message is None or not success_message.is_displayed():
            self.fail("Order success message is not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()