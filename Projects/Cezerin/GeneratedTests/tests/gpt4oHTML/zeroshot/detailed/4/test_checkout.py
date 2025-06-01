import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("about:blank")

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open home page
        driver.get("data:text/html;charset=utf-8," + html_data['home_page'])

        # Step 2: Click on product category
        try:
            category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
            category_link.click()
        except:
            self.fail("Category link not found")

        # Step 3: Select the first product
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_link.click()
        except:
            self.fail("Product link not found")

        # Step 4: Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Step 5: Click the cart icon/button to open the shopping bag
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout']"))
            )
        except:
            self.fail("GO TO CHECKOUT button not found")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
        except:
            self.fail("Checkout form did not appear")

        # Step 9: Fill out the checkout form fields
        email_field.send_keys("mail@mail.com")
        driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
        driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
        driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        driver.find_element(By.XPATH, "//input[@name='shipping_method_id']").click()
        driver.find_element(By.XPATH, "//input[@name='payment_method_id']").click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button")
        next_button.click()

        # Step 12: Click the "Place Order" button
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.is-primary[type='submit']"))
            )
            place_order_button.click()
        except:
            self.fail("Place Order button not found")

        # Step 13: Check that the confirmation page includes the text "Thanks for your order!"
        try:
            success_text = WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".checkout-success-title"), "Thanks for your order!")
            )
            self.assertTrue(success_text)
        except:
            self.fail("Confirmation text not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()