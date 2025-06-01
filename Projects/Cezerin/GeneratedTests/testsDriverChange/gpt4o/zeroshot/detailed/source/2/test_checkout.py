import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on product category
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a"]'))).click()

        # Step 3: Select the first product
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))).click()

        # Step 4: Click the "Add to cart" button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button'))).click()

        # Step 5: Click the cart icon/button to open the shopping bag
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button'))).click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        checkout_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[href="/checkout"]')
        ))

        if not checkout_button or checkout_button.text.strip() == "":
            self.fail("GO TO CHECKOUT button is not present inside the cart.")

        # Step 7: Click the "GO TO CHECKOUT" button
        checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        wait.until(EC.presence_of_element_located((By.ID, 'customer.email')))

        # Step 9: Fill out the checkout form
        driver.find_element(By.ID, 'customer.email').send_keys('mail@mail.com')
        driver.find_element(By.ID, 'customer.mobile').send_keys('12345678')
        driver.find_element(By.ID, 'shipping_address.state').send_keys('Riga')
        driver.find_element(By.ID, 'shipping_address.city').send_keys('Riga')

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, 'input[name="shipping_method_id"]')
        payment_method = driver.find_element(By.CSS_SELECTOR, 'input[name="payment_method_id"]')
        if not shipping_method:
            self.fail("Shipping method is not available.")
        if not payment_method:
            self.fail("Payment method is not available.")
        shipping_method.click()
        payment_method.click()

        # Step 11: Click the "Next" button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button-wrap button'))).click()

        # Step 12: Click the "Place Order" button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

        # Step 13: Wait for confirmation page and check that it includes the text
        confirmation = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.checkout-success-title')
        ))
        if not confirmation or 'Thanks for your order!' not in confirmation.text:
            self.fail("Order confirmation message is missing or incorrect.")

if __name__ == "__main__":
    unittest.main()