import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=Options(headless=False))

    def test_shopping_cart(self):
        # Step 1: Open home page
        self.driver.get('http://localhost:3000/')  # replace with your website URL

        # Step 2: Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/category"]'))).click()

        # Step 3: Select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="product-item"]/a'))).click()

        # Step 4: Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-action="add-to-cart"]'))).click()

        # Step 5: Click the cart icon/button to open the shopping bag
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-button'))).click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@data-action="go-to-checkout"]')))
        self.assertTrue(go_to_checkout_button.is_enabled())

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'checkout-form')))

        # Step 9: Fill out the checkout form fields using the following credentials:
        self.driver.find_element(By.NAME, 'email').send_keys('mail@mail.com')
        self.driver.find_element(By.NAME, 'phone').send_keys('12345678')

        # Step 10: Select a shipping method and a payment method
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//select[@name="shipping-method"]'))).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@type="radio"][1]'))).click()

        # Step 11: Click the "Next" button
        self.driver.find_element(By.NAME, 'next').click()

        # Step 12: Click the "Place Order" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-action="place-order"]'))).click()

        # Step 13: Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        success_page_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="success-page"]/h2')))
        self.assertEqual(success_page_text.text.strip(), 'Thanks for your order!')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()