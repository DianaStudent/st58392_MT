from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        homepage_title = driver.title
        self.assertTrue("nopCommerce" in homepage_title, f"Unexpected page title: {homepage_title}")

        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Search for a product (e.g. "book")
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
        search_button.click()

        # Step 4: Add to cart the first item from search results
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 5: Open the shopping cart via the success notification popup
        cart_notification_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "shopping cart"))
        )
        cart_notification_link.click()

        # Step 6: Accept terms of service and click the "Checkout" button
        terms_checkbox = wait.until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 7: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 8: Fill in the billing address
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        # Continue to next step
        driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button").click()

        # Step 9: Select shipping method
        wait.until(
            EC.presence_of_element_located((By.ID, "shippingoption_1"))
        ).click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        # Step 10: Select payment method
        wait.until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        ).click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Step 11: Enter credit card details
        wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))).send_keys("Visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        # Continue to confirm order
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Step 12: Confirm the order
        confirm_order_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Step 13: Validate that the confirmation message or success section is visible
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed .title"))
        ).text
        self.assertTrue("Your order has been successfully processed!" in success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()