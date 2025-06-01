from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_checkout_simple(self):
        # After adding a product to the cart, the test must click on the cart button (shopping bag)
        cart_button_locator = (By.XPATH, "//a[@class='cart']")  # Adjust this locator as per your actual HTML structure
        self.failUnless(cart_button_locator, "Cart button not found")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(cart_button_locator)).click()

        # Wait for presence of "GO TO CHECKOUT" button using html_data.
        go_to_checkout_button_locator = (By.XPATH, "//button[@class='go-to-checkout']")  # Adjust this locator as per your actual HTML structure
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(go_to_checkout_button_locator)).click()

        # Fill required checkout fields
        email_field_locator = (By.NAME, "email")
        self.failUnless(email_field_locator, "Email field not found")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(email_field_locator)).send_keys("your_email@gmail.com")  # Replace this with actual email value

        phone_number_field_locator = (By.XPATH, "//input[@name='phone']")  # Adjust this locator as per your actual HTML structure
        self.failUnless(phone_number_field_locator, "Phone number field not found")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(phone_number_field_locator)).send_keys("1234567890")

        shipping_address_field_locator = (By.XPATH, "//textarea[@name='shippingAddress']")  # Adjust this locator as per your actual HTML structure
        self.failUnless(shipping_address_field_locator, "Shipping address field not found")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(shipping_address_field_locator)).send_keys("Your shipping address")

        # Place order
        place_order_button_locator = (By.XPATH, "//button[@class='place-order']")  # Adjust this locator as per your actual HTML structure
        self.failUnless(place_order_button_locator, "Place order button not found")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(place_order_button_locator)).click()

        # Confirm that the final success page contains the text: "Thanks for your order!"
        thanks_for_your_order_text_locator = (By.XPATH, "//h2[@class='thanks-for-your-order']")  # Adjust this locator as per your actual HTML structure
        self.failUnless(thanks_for_your_order_text_locator, "Thanks for your order! text not found")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(thanks_for_your_order_text_locator))
        final_success_page_text = self.driver.find_element(By.XPATH, "//h2[@class='thanks-for-your-order']").text
        self.assertEqual(final_success_page_text, "Thanks for your order!", "Final success page text mismatch")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()