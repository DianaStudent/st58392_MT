import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the search page
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()
        
        # Search for "book"
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        search_button.click()

        # Add first item to cart
        first_product_add_to_cart = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        first_product_add_to_cart.click()

        # Open shopping cart from success notification
        cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_button.click()

        # Proceed to checkout
        terms_service_checkbox = wait.until(
            EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_service_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Checkout as guest
        checkout_as_guest_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing address
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        driver.find_element(By.NAME, "save").click()

        # Select shipping method
        wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1"))).click()
        driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button").click()

        # Select payment method
        wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1"))).click()
        driver.find_element(By.CLASS_NAME, "payment-method-next-step-button").click()

        # Enter payment info
        wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))).send_keys("Visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.CLASS_NAME, "payment-info-next-step-button").click()

        # Confirm order
        confirm_order_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify order completion
        order_completed_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "order-completed"))
        )
        if not order_completed_message:
            self.fail("Order completion message not found or empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()