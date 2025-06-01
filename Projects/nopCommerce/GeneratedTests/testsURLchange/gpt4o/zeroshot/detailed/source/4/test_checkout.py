from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # 1. Open the homepage.
        driver.get("http://max/")

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 search-button']")))
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-2 product-box-add-to-cart-button']")))
        add_to_cart_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill out the full billing form.
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        
        country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_dropdown.find_element(By.CSS_SELECTOR, "option[value='124']").click()

        continue_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 new-address-next-step-button']")))
        continue_button.click()

        # 8. Proceed through the following:
        # - Shipping method step.
        shipping_method_continue = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']")))
        shipping_method_continue.click()

        # - Payment method step.
        payment_method_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='paymentmethod_1']")))
        payment_method_radio.click()
        payment_method_continue = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 payment-method-next-step-button']")))
        payment_method_continue.click()

        # - Payment info step.
        credit_card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        credit_card_type.find_element(By.CSS_SELECTOR, "option[value='visa']").click()
        
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        
        expire_month = driver.find_element(By.ID, "ExpireMonth")
        expire_month.find_element(By.CSS_SELECTOR, "option[value='4']").click()
        
        expire_year = driver.find_element(By.ID, "ExpireYear")
        expire_year.find_element(By.CSS_SELECTOR, "option[value='2027']").click()
        
        driver.find_element(By.ID, "CardCode").send_keys("123")
        
        payment_info_continue = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 payment-info-next-step-button']")))
        payment_info_continue.click()

        # 9. On the confirm step, click “Confirm” and wait for the success message.
        confirm_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 confirm-order-next-step-button']")))
        confirm_order_button.click()

        # 10. Confirm that the order has been completed by checking the confirmation text "Thank you".
        thank_you_text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1")))
        self.assertEqual("Thank you", thank_you_text.text, "Order completion failed or 'Thank you' text not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()