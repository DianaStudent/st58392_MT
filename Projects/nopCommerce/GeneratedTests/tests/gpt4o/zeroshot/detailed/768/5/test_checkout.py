from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        
        # 1. Navigate to Search page
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search"))).click()
        
        # 2. Search for a product
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button"))).click()
        
        # 3. Add first result to cart
        add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        if not add_to_cart_buttons:
            self.fail("No products found or 'Add to cart' button missing.")
        add_to_cart_buttons[0].click()

        # 4. Click on the shopping cart link from success notification
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification"))).click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart"))).click()

        # 5. Checkout process from cart
        self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()
        
        # 6. Checkout as Guest
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button"))).click()
        
        # 7. Fill billing form
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        # Select Country and State
        country_select = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_select.find_element(By.CSS_SELECTOR, "option[value='124']").click()

        state_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        state_select.find_element(By.CSS_SELECTOR, "option[value='0']").click()
        
        self.wait.until(EC.presence_of_element_located((By.NAME, "save"))).click()

        # 8. Proceed through shipping method
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shippingoption_1"))).click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button"))).click()

        # 9. Payment method
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))).click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button"))).click()

        # 10. Payment information (if required)
        self.wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button"))).click()

        # Confirm Order
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button"))).click()

        # 11. Verify order completion
        success_message = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual("Thank you", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()