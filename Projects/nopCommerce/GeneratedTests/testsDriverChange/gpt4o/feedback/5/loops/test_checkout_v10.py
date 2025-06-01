from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the "Search" page
        search_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_menu.click()

        # Search for a product
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("book")
        driver.find_element(By.CLASS_NAME, "search-box-button").click()

        # Add the first result to the cart
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        if not add_to_cart_buttons:
            self.fail("Add to cart buttons not found.")
        add_to_cart_buttons[0].click()

        # Click the "shopping cart" link from the success notification
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Check the "Terms of service" checkbox and click "Checkout"
        terms_of_service = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Choose "Checkout as Guest"
        checkout_as_guest = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest.click()

        # Fill out billing form
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("user_zz18872z@test.com")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        # Select Country
        country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_dropdown.find_element(By.CSS_SELECTOR, "option[value='237']").click()

        # Select State/Province
        state_dropdown = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        state_dropdown.find_element(By.CSS_SELECTOR, "option[value='0']").click()

        billing_continue = wait.until(EC.element_to_be_clickable((By.NAME, "save")))
        billing_continue.click()

        # Select shipping method
        shipping_method_radio = wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_method_radio.click()
        driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button").click()

        # Select payment method
        wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1"))).click()
        driver.find_element(By.CLASS_NAME, "payment-method-next-step-button").click()

        # Fill payment information
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("4")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.CLASS_NAME, "payment-info-next-step-button").click()

        # Confirm order
        confirm_order_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify order completion
        thank_you_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        self.assertIn("Thank you", thank_you_text, "Order completion message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()