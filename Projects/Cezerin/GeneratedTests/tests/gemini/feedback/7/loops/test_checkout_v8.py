import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # 1. Open home page.
        # 2. Click on product category.
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except TimeoutException:
            self.fail("Category A link not found or not clickable")

        # 3. Select the first product.
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()
        except TimeoutException:
            self.fail("Product A link not found or not clickable")

        # 4. Click the "Add to cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Add to cart button not found or not clickable")

        # 5. Click the cart icon/button to open the shopping bag.
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except TimeoutException:
            self.fail("Cart button not found or not clickable")

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not present")
        except TimeoutException:
            self.fail("GO TO CHECKOUT button is not present")

        # 7. Click the "GO TO CHECKOUT" button.
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except TimeoutException:
            self.fail("GO TO CHECKOUT button not found or not clickable")

        # 8. Wait for the checkout form to appear.
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
        except TimeoutException:
            self.fail("Checkout form (email field) did not appear")

        # 9. Fill out the checkout form fields.
        email_field.send_keys("mail@mail.com")
        phone_field = driver.find_element(By.ID, "customer.mobile")
        phone_field.send_keys("12345678")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # 10. Select a shipping method and a payment method.
        try:
            shipping_method_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "shipping_method_id"))
            )
            shipping_method_radio.click()
        except TimeoutException:
            self.fail("Shipping method radio button not found or not clickable")

        try:
            payment_method_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "payment_method_id"))
            )
            payment_method_radio.click()
        except TimeoutException:
            self.fail("Payment method radio button not found or not clickable")

        # 11. Click the "Next" button.
        try:
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
            )
            next_button.click()
        except TimeoutException:
            self.fail("Next button not found or not clickable")

        # 12. Click the "Place Order" button.
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))
            )
            place_order_button.click()
        except TimeoutException:
            self.fail("Place Order button not found or not clickable")

        # 13. Wait for the confirmation page and check that it includes the text "Thanks for your order!".
        try:
            confirmation_text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
            )
            if confirmation_text and confirmation_text.text:
                self.assertTrue("Thanks for your order!" in confirmation_text.text, "Confirmation text is not present")
            else:
                self.fail("Confirmation text element is empty")
        except TimeoutException:
            self.fail("Confirmation page did not appear or confirmation text not found")

if __name__ == "__main__":
    unittest.main()