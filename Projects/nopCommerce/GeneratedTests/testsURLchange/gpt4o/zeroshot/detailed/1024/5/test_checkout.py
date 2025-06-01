import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def test_user_checkout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get(self.base_url)
        
        # Step 2: Navigate to the "Search" page and look for a product using the query "book"
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-box-button")
        search_button.click()

        # Step 3: Add the first result to the cart using a product tile button
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        if not add_to_cart_buttons:
            self.fail("No products found to add to cart.")
        add_to_cart_buttons[0].click()

        # Step 4: From the success notification, click the "shopping cart" link
        cart_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 5: Check the "Terms of service" checkbox and click the "Checkout" button
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill out the billing form
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        billing_continue_button = driver.find_element(By.CSS_SELECTOR, "#billing-buttons-container .new-address-next-step-button")
        billing_continue_button.click()
        
        # Step 8: Proceed through the shipping method, payment method, and payment info steps
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shipping-method-buttons-container .shipping-method-next-step-button"))).click()
        
        wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1"))).click()
        driver.find_element(By.CSS_SELECTOR, "#shipping-method-buttons-container .shipping-method-next-step-button").click()
        
        wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1"))).click()
        driver.find_element(By.CSS_SELECTOR, "#payment-method-buttons-container .payment-method-next-step-button").click()
        
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("4")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#payment-info-buttons-container .payment-info-next-step-button").click()
        
        # Step 9: Confirm the order
        confirm_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#confirm-order-buttons-container .confirm-order-next-step-button")))
        confirm_button.click()
        
        # Step 10: Verify order completion
        thank_you_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']")))
        self.assertIsNotNone(thank_you_text, "Order completion message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()