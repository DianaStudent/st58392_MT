from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")  # Replace with the actual website URL
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to category A page and product A page
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            ).click()

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            ).click()
        except Exception as e:
            self.fail(f"Failed to navigate to product page: {str(e)}")

        # Add product to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-addtocart"))
            ).find_element(By.TAG_NAME, "button")
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {str(e)}")
        
        # Open cart and go to checkout
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()

            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to open cart or go to checkout: {str(e)}")

        # Fill required checkout fields and place order
        try:
            # Fill customer details
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            ).send_keys("mail@mail.com")

            driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
            driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
            driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

            # Select shipping and payment method
            shipping_method = driver.find_element(By.NAME, "shipping_method_id")
            payment_method = driver.find_element(By.NAME, "payment_method_id")

            shipping_method.click()
            payment_method.click()

            # Place order
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.is-primary"))
            )
            place_order_button.click()
        except Exception as e:
            self.fail(f"Failed during checkout: {str(e)}")

        # Confirm success message on the final page
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
            )
            self.assertTrue("Thanks for your order!" in success_message.text)
        except Exception as e:
            self.fail(f"Order completion confirmation failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()