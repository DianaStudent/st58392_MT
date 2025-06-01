import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestECommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_checkout_process(self):
        # Click on the menu button
        menu_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='menubar']/button")))
        menu_button.click()

        # Click on the "Store" link
        store_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='dropdown-menu']/li[2]/a")))
        store_link.click()

        # Click on a product image (thumbnail)
        product_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='product-image']")))
        product_image.click()

        # Select a size
        select_size_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart']")))
        select_size_button.click()

        # Click the cart button to open the cart
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='shopping-bag']")))
        cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button using html_data
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']")))
        go_to_checkout_button.click()

        # Fill required checkout fields
        first_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'first_name')))
        last_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'last_name')))
        address_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'address')))
        postal_code_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'postal_code')))
        city_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'city')))
        country_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'country')))
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))

        first_name_field.send_keys("user")
        last_name_field.send_keys("test")
        address_field.send_keys("street 1")
        postal_code_field.send_keys("LV-1021")
        city_field.send_keys("Riga")
        country_field.send_keys("Denmark")
        email_field.send_keys("user@test.com")

        # Select delivery and payment methods
        select_delivery_method = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@name='shipping_method']")))
        select_payment_method = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@name='payment_method']")))

        # Select delivery method
        select_delivery_method.click()
        delivery_option = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//option[text()='Free Delivery']")))
        delivery_option.click()

        # Select payment method
        select_payment_method.click()
        payment_option = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//option[text()='PayPal']")))
        payment_option.click()

        # Click "Place Order"
        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='place-order']")))
        place_order_button.click()

        # Verify the confirmation page contains: "Your order was placed successfully"
        success_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Your order has been successfully placed.']")))
        self.assertEqual(success_text.text, 'Your order has been successfully placed.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()