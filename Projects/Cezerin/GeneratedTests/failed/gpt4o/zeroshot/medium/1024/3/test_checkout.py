from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        home_page_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logo-image")))
        self.assertIsNotNone(home_page_title)

        # Step 2: Click on product category
        category_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # Step 3: Select the first product
        product_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Go to checkout']")))
        self.assertIsNotNone(go_to_checkout_button)

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Fill required checkout fields
        wait.until(EC.element_to_be_clickable((By.ID, "customer.email"))).send_keys("mail@mail.com")
        wait.until(EC.element_to_be_clickable((By.ID, "customer.mobile"))).send_keys("12345678")
        wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.state"))).send_keys("Riga")
        wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.city"))).send_keys("Riga")

        # Step 9: Select a shipping and payment method
        shipping_method = wait.until(EC.element_to_be_clickable((By.NAME, "shipping_method_id")))
        shipping_method.click()
        payment_method = wait.until(EC.element_to_be_clickable((By.NAME, "payment_method_id")))
        payment_method.click()

        # Step 10: Click "Next" and then "Place Order" to complete the process
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
        next_button.click()
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIsNotNone(success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()