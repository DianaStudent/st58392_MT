```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        self.assertEqual(driver.current_url, "http://max/")

        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']")))
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        terms_of_service_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill in the billing address.
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys("Test")

        last_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName")))
        last_name_input.send_keys("User")

        email_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email")))
        email_input.send_keys("random_email")

        country_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send_keys(Keys.ARROW_DOWN)
        country_select.send