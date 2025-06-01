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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Search for a product (e.g. “book”)
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Add the first product to the cart
        add_to_cart_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_btn.click()

        # Click “shopping cart” from the success popup
        go_to_cart_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".content a[href='/cart']")))
        go_to_cart_btn.click()

        # Proceed to checkout as a guest
        checkout_as_guest_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_btn.click()

        # Fill the billing form
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")

        # Continue to the next step
        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # Select shipping method
        wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1"))).click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        # Select payment method
        wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1"))).click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Enter payment information
        wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        # Continue to confirm order
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Confirm order
        confirm_order_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_btn.click()

        # Verify order completion
        thank_you_header = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".page-title h1")))

        self.assertEqual(thank_you_header.text, "Thank you", "Order was not completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()