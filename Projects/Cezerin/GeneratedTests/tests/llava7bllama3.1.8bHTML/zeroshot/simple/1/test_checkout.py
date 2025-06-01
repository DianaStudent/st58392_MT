from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://your-store.com")  # Replace with your store URL

    def test_checkout_process(self):
        try:
            # Add a product to the cart
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']"))).click()

            # Click on the cart button (shopping bag)
            cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='cart-icon']")))
            cart_button.click()

            # Wait for presence of "GO TO CHECKOUT" button
            checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Proceed to Checkout']")))

            # Fill required checkout fields
            email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
            email_input.send_keys("your_email@example.com")  # Replace with your email

            phone_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "phone")))
            phone_input.send_keys("(207) 564-8482")

            shipping_address_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "shipping-address")))
            shipping_address_input.send_keys("104 N Stagecoach Rd\nDover Foxcroft, ME, 04426")

            shipping_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@name='shipping']")))
            shipping_select.select_by_value("Standard Shipping")

            payment_method_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@name='payment-method']")))
            payment_method_select.select_by_value("PayPal")

            # Place the order
            checkout_button.click()

            # Wait for final success page to load
            final_success_page = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Thanks for your order!']")))

            self.assertTrue(final_success_page.text == "Thanks for your order!")

        except TimeoutException:
            self.fail("Required elements are missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()