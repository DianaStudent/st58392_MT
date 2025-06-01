from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        driver = self.driver

        # Open category page
        category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        category_link.click()

        # Select the first product
        product_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        product_link.click()
        
        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.button-addtocart .button'))
        )
        add_to_cart_button.click()

        # Open the shopping bag
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-button'))
        )
        cart_button.click()

        # Verify "GO TO CHECKOUT" button is present
        checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]'))
        )
        self.assertTrue(checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")
        checkout_button.click()

        # Wait for the checkout form to appear and fill out the form
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#customer\\.email'))
        )
        driver.find_element(By.CSS_SELECTOR, '#customer\\.email').send_keys("mail@mail.com")
        driver.find_element(By.CSS_SELECTOR, '#customer\\.mobile').send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, '#shipping_address\\.state').send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, '#shipping_address\\.city').send_keys("Riga")

        # Select a shipping method
        shipping_method = driver.find_element(By.CSS_SELECTOR, 'input[name=shipping_method_id]')
        if not shipping_method.is_selected():
            shipping_method.click()

        # Select a payment method
        payment_method = driver.find_element(By.CSS_SELECTOR, 'input[name=payment_method_id]')
        if not payment_method.is_selected():
            payment_method.click()

        # Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, '.checkout-button-wrap .button')
        next_button.click()

        # Click the "Place Order" button
        place_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button.button.is-primary'))
        )
        place_order_button.click()

        # Verify the order confirmation page
        confirmation_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Thanks for your order!")]'))
        )
        self.assertIsNotNone(confirmation_text, "Order confirmation text is not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()