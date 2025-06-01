from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_checkout_process(self):
        # Navigate to home page
        self.driver.get("http://localhost/")

        # Login using credentials
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "login")))
        login_button.click()

        username_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "username")))
        username_input.send_keys("test22@user.com")

        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_input.send_keys("test**11")

        login_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "login-form")))
        login_form.submit()

        # Navigate back to home page
        self.driver.get("http://localhost/")

        # Hover over the first product
        product_list = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='products']/li[1]")))
        product_list.find_element(By.TAG_NAME, "a").click()

        # Click the revealed 'Add to cart' button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
        add_to_cart_button.click()

        # Open popup cart
        cart_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "cart-icon")))
        cart_icon.click()

        # Wait for popup to become visible
        popup_visible = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "popup-cart")))

        # Click 'View cart' button inside the popup
        view_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "view-cart")))
        view_cart_button.click()

        # On the cart page, click the 'Proceed to Checkout' button
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "proceed-to-checkout")))
        proceed_to_checkout_button.click()

        # Fill out the billing form:
        company_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "company")))
        company_input.send_keys("Comp1")

        address_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "address")))
        address_input.send_keys("Street1")

        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "city")))
        city_input.send_keys("Quebec")

        # Select region/state from dropdown
        region_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "region-dropdown")))
        region_dropdown.find_element(By.XPATH, "//option[1]").click()

        postal_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "postal-code")))
        postal_code_input.send_keys("1234")

        phone_number_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "phone-number")))
        phone_number_input.send_keys("1234567891")

        # Accept terms checkbox
        accept_terms_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "accept-terms")))
        accept_terms_checkbox.click()

        # Confirm success if form is filled
        self.assertTrue(company_input.get_attribute('value') == 'Comp1')
        self.assertTrue(address_input.get_attribute('value') == 'Street1')
        self.assertTrue(city_input.get_attribute('value') == 'Quebec')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()