from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage.
        # Already on the homepage

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        search_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/search']")))
        search_link.click()

        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bar-notification.success a[href='/cart']")))
        cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill out the full billing form with credentials.
        billing_first_name = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        billing_first_name.send_keys("Test")
        billing_last_name = driver.find_element(By.ID, "BillingNewAddress_LastName")
        billing_last_name.send_keys("User")
        billing_email = driver.find_element(By.ID, "BillingNewAddress_Email")
        billing_email.send_keys("random_email@test.com")
        billing_city = driver.find_element(By.ID, "BillingNewAddress_City")
        billing_city.send_keys("Riga")
        billing_address1 = driver.find_element(By.ID, "BillingNewAddress_Address1")
        billing_address1.send_keys("Street 1")
        billing_zip = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        billing_zip.send_keys("LV-1234")
        billing_phone = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        billing_phone.send_keys("12345678")

        billing_country = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        billing_country.send_keys("Latvia")
        billing_state = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        billing_state.send_keys("Other")

        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # 8. Proceed through the following steps:
        # Shipping method step.
        shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        shipping_continue_button.click()

        # Payment method step.
        payment_method_radio = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method_radio.click()
        payment_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        # Payment info step.
        wait.until(EC.element_to_be_clickable((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        payment_info_continue = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue.click()

        # 9. On the confirm step, click “Confirm” and wait for the success message.
        confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_button.click()

        # 10. Confirm that the order has been completed by checking for the confirmation message "Thank you".
        thank_you_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title h1")))
        self.assertTrue(thank_you_message and thank_you_message.text == "Thank you")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()