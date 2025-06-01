import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_checkout(self):
        self.driver.get("http://localhost:8000/dk")
        menu_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='menu-button']")))
        menu_button.click()
        
        store_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        product_image = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='/assets/img/products/1.jpg']")))
        product_image.click()

        size_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='size-button']")))
        size_button.click()
        
        # Add product to cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-to-cart-button']")))
        add_to_cart_button.click()

        # Click on the cart button
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='cart-button']")))
        cart_button.click()
        
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-checkout-button']")))
        go_to_checkout_button.click()

        # Fill required checkout fields
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "first_name")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "last_name")))
        address_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "address")))
        postal_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "postal_code")))
        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "city")))
        country_combo_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "country")))
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        address_input.send_keys("street 1")
        postal_code_input.send_keys("LV-1021")
        city_input.send_keys("Riga")
        country_combo_box.click()
        # Select Denmark from combo box
        denmark_option = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//option[@value='Denmark']")))
        denmark_option.click()
        email_input.send_keys("user@test.com")

        continue_to_delivery_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-to-delivery-button']")))
        continue_to_delivery_button.click()

        delivery_method_radio_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "delivery_method")))

        # Select radio button
        denmark_radio_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Denmark']")))
        denmark_radio_button.click()

        continue_to_payment_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-to-payment-button']")))
        continue_to_payment_button.click()

        payment_method_radio_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "payment_method")))

        # Select radio button
        bank_transfer_radio_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Bank Transfer']")))
        bank_transfer_radio_button.click()

        continue_to_review_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-to-review-button']")))
        continue_to_review_button.click()

        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='place-order-button']")))
        place_order_button.click()

        # Verify that the order has been placed successfully
        success_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-message']")))

    def test_checkout_successfully(self):
        self.assertEqual(success_message.text, "Order has been placed successfully")

if __name__ == "__main__":
    unittest.main()