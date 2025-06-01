import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestOrderProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_order_process(self):
        # 1. Open the homepage.
        self.driver.get("http://max/")

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        search_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search_query_top")))
        search_box.send_keys("book")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "#searchbox > button")
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        product_tile_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@id='center_column']//li[1]//div[2]/div[1]/a")))
        product_tile_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        shopping_cart_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_only'][contains(text(), 'Shopping Cart')]")))
        shopping_cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, ".button-container > a.button")
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        guest_checkout_option = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "guest_email")))
        guest_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "checkout_as_guest")))
        guest_checkbox.click()
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "#form > a")
        continue_button.click()

        # 7. Fill out the full billing form.
        first_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "firstname")))
        last_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "lastname")))
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        address_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "address1")))
        city_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "city")))
        country_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "country_id")))
        zip_code_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "postcode")))
        phone_number_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "phone")))

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        email_field.send_keys("random_email")
        address_field.send_keys("Street 1")
        city_field.send_keys("Riga")
        country_select.send_keys("124")
        zip_code_field.send_keys("LV-1234")
        phone_number_field.send_keys("12345678")

        # Proceed through the following steps.
        shipping_method_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_method_button.click()
        payment_method_option = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@value='visa']")))
        payment_method_option.click()

        # Payment info step (fill in credit card details if necessary).
        cardholder_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardholdername")))
        card_number_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cc_number")))
        expire_month_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cc_expire_month")))
        expire_year_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cc_expire_year")))
        cardholder_name_field.send_keys("Test User")
        card_number_field.send_keys("1234567890123456")
        expire_month_field.send_keys("12")
        expire_year_field.send_keys("2025")

        # 8. Place the order.
        confirm_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "confirmorder")))
        confirm_button.click()

        # Verify that the order was placed successfully.
        order_number_label = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fancybox-title']")))
        self.assertEqual(order_number_label.text, "Order confirmation")

if __name__ == "__main__":
    unittest.main()