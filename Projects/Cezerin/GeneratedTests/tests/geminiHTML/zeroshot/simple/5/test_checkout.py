import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Go to Category A page
        try:
            category_a_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except:
            self.fail("Category A link not found")

        # 2. Go to Product A page
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()
        except:
            self.fail("Product A link not found")

        # 3. Add product to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # 4. Click on the cart button
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # 5. Click on "Go to checkout" button
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Go to checkout button not found")

        # 6. Fill customer details
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
            email_field.send_keys("mail@mail.com")

            mobile_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.mobile"))
            )
            mobile_field.send_keys("12345678")

            state_field = wait.until(
                EC.presence_of_element_located((By.ID, "shipping_address.state"))
            )
            state_field.send_keys("Riga")

            city_field = wait.until(
                EC.presence_of_element_located((By.ID, "shipping_address.city"))
            )
            city_field.send_keys("Riga")

        except:
            self.fail("Could not fill customer details")

        # 7. Select shipping and payment methods and click next
        try:
            shipping_method = wait.until(
                EC.element_to_be_clickable((By.NAME, "shipping_method_id"))
            )
            shipping_method.click()

            payment_method = wait.until(
                EC.element_to_be_clickable((By.NAME, "payment_method_id"))
            )
            payment_method.click()

            next_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.is-primary"))
            )
            next_button.click()
        except:
            self.fail("Could not select shipping/payment methods and click next")

        # 8. Fill comments
        try:
            comments_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.comments"))
            )
            comments_field.send_keys("Test comment")
        except:
            self.fail("Could not fill comments")

        # 9. Place order
        try:
            place_order_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.is-primary"))
            )
            place_order_button.click()
        except:
            self.fail("Place order button not found")

        # 10. Verify success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "checkout-success-title"))
            )
            self.assertIn("Thanks for your order!", success_message.text)
        except:
            self.fail("Success message not found or incorrect")


if __name__ == "__main__":
    unittest.main()