import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://max/"

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the home page
        driver.get(self.base_url)
        
        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        
        # Step 2: Search for a product (e.g. "book")
        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")
        search_input.send_keys(Keys.ENTER)
        
        # Step 3: Click "Add to cart" for the first item in search results
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()
        
        # Step 4: Open the shopping cart via the success notification popup
        go_to_cart_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "shopping cart")))
        go_to_cart_button.click()

        # Step 5: Accept terms of service and click "Checkout"
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_checkbox.click()
        
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()
        
        # Step 7: Fill in the billing address
        wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        
        continue_button = driver.find_element(By.CSS_SELECTOR, "#billing-buttons-container button")
        continue_button.click()
        
        # Step 8: Select shipping method
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ShippingOption))).click()
        
        shipping_continue_button = driver.find_element(By.CSS_SELECTOR, "#shipping-method-buttons-container button")
        shipping_continue_button.click()

        # Step 8: Select payment method
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, PaymentMethodOption))).click()

        payment_continue_button = driver.find_element(By.CSS_SELECTOR, "#payment-method-buttons-container button")
        payment_continue_button.click()

        # Step 9: Enter credit card details
        wait.until(EC.element_to_be_clickable((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("4")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, "#payment-info-buttons-container button")
        payment_info_continue_button.click()

        # Step 10: Confirm the order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirm-order-buttons-container button")))
        confirm_order_button.click()

        # Step 11: Validate that the confirmation message is visible
        confirmation_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='section order-completed']")))
        
        if not confirmation_message or not confirmation_message.text.strip():
            self.fail("Order confirmation message not found.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()