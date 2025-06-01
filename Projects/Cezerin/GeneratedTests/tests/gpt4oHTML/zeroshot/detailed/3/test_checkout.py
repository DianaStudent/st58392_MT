import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # Replace with actual URL

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Step 1. Open home page.
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "logo-image")))

        # Step 2. Click on product category.
        category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_link.click()

        # Step 3. Select the first product.
        first_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        first_product.click()

        # Step 4. Click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button-addtocart') and contains(@class, 'is-success')]"))
        )
        add_to_cart_button.click()

        # Step 5. Click the cart icon/button to open the shopping bag.
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        cart_button.click()

        # Step 6. Verify that the "Go to checkout" button is present inside the cart.
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'button') and contains(text(), 'Go to checkout')]"))
        )
        assert go_to_checkout_button.is_displayed()

        # Step 7. Click the "Go to checkout" button.
        go_to_checkout_button.click()

        # Step 8. Wait for the checkout form to appear.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )

        # Step 9. Fill out the checkout form fields using given credentials.
        driver.find_element(By.ID, "customer.email").send_keys("mail@mail.com")
        driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
        driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
        driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

        # Step 10. Select a shipping method and a payment method.
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id'][1]")
        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id'][1]")
        
        if shipping_method.is_displayed() and not shipping_method.is_selected():
            shipping_method.click()
        
        if payment_method.is_displayed() and not payment_method.is_selected():
            payment_method.click()

        # Step 11. Click the "Next" button.
        next_button = driver.find_element(By.XPATH, "//button[contains(@class, 'checkout-button') and contains(text(), 'Next')]")
        next_button.click()

        # Step 12. Click the "Place Order" button.
        place_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'checkout-button') and contains(text(), 'Place Order')]"))
        )
        place_order_button.click()

        # Step 13. Wait for the confirmation page and check that it includes the text "Thanks for your order!".
        confirmation_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertTrue(confirmation_text.is_displayed())

if __name__ == "__main__":
    unittest.main()