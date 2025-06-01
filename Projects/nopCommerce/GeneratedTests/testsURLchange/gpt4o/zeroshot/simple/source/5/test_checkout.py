import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_checkout_process(self):
        driver = self.driver
        
        # Search for a product
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results and add the first product to the cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Wait for the success popup and click on the 'shopping cart' link
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
        )
        cart_link = driver.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Proceed to checkout
        checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        checkout_button.click()

        # Checkout as guest
        guest_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button-1.checkout-as-guest-button"))
        )
        guest_checkout_button.click()

        # Fill billing form
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        billing_continue_button = driver.find_element(By.NAME, "save")
        billing_continue_button.click()

        # Select shipping method and continue
        shipping_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "shippingoption_1"))
        )
        shipping_option.click()

        shipping_continue_button = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue_button.click()

        # Select payment method and continue
        payment_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        )
        payment_option.click()

        payment_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        # Fill payment info
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        )
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_button.click()

        # Confirm order
        confirm_order_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Check for order completion
        thank_you_header = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-title"))
        )
        self.assertIn("Thank you", thank_you_header.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()