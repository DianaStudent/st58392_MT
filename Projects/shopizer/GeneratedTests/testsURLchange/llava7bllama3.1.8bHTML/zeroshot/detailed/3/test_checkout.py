import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCartCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_cart_checkout(self):
        # Login
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys("test22@user.com")
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("test**11")
        self.driver.find_element(By.NAME, "login").click()

        # Navigate back to home page
        self.driver.back()
        self.driver.forward()

        # Hover over first product and click Add to Cart
        product = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product']")))
        product.hover()
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class,'add-to-cart')])[1]")))
        add_to_cart_button.click()

        # Open popup cart
        cart_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cart-icon")))
        cart_icon.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Click View Cart or similar button inside popup
        view_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'View Cart')]")))
        view_cart_button.click()

        # On cart page click Proceed to Checkout
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Proceed to Checkout')]")))
        proceed_to_checkout_button.click()

        # Fill out billing form
        company_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "Company")))
        company_input.send_keys("Comp1")
        address_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "Address")))
        address_input.send_keys("Street1")
        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "City")))
        city_input.send_keys("Quebec")

        # Select region/state from dropdown
        state_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@class='form-control']")))
        state_option = self.driver.find_element(By.XPATH, "(//option[contains(text(),'Select region / State')])[2]")
        state_dropdown.send_keys(state_option.text)
        region_state = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//option[@value='Quebec']")))
        region_state.click()

        # Fill out other fields
        postal_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "PostalCode")))
        postal_code_input.send_keys("1234")
        phone_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "Phone")))
        phone_number_input.send_keys("1234567891")

        # Accept terms checkbox
        accept_terms_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@class='form-check-input']")))
        if not accept_terms_checkbox.is_selected():
            accept_terms_checkbox.click()

        # Wait for any maps popups or warnings and close them
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "map-popup")))

        # Confirm success if form is filled
        company_input_value = company_input.get_attribute("value")
        address_input_value = address_input.get_attribute("value")
        city_input_value = city_input.get_attribute("value")
        state_dropdown_value = state_dropdown.get_attribute("value")
        postal_code_input_value = postal_code_input.get_attribute("value")
        phone_number_input_value = phone_number_input.get_attribute("value")

        if company_input_value and address_input_value and city_input_value and state_dropdown_value and postal_code_input_value and phone_number_input_value:
            self.assertTrue(True)
        else:
            self.fail("Billing form not filled correctly")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()