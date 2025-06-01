import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Open home page
        driver.get("http://localhost:3000/")

        # Click on product category (Category A)
        category_a = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # Select the first product (Product A)
        product_a = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]")))

        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Wait for the checkout form to appear
        customer_email = self.wait.until(EC.presence_of_element_located(
            (By.ID, "customer.email")))

        # Fill out the checkout form fields
        customer_email.send_keys("mail@mail.com")
        driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
        driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
        driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

        # Select a shipping method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        driver.execute_script("arguments[0].click();", shipping_method)

        # Select a payment method
        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        driver.execute_script("arguments[0].click();", payment_method)

        # Click the "Next" button
        next_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Next')]")))
        next_button.click()

        # Click the "Place Order" button
        place_order_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Place Order')]")))
        place_order_button.click()

        # Wait for the confirmation page
        confirmation_page = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))

        if not confirmation_page:
            self.fail("Order confirmation page not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()