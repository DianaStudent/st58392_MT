from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckout(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.find_element(By.NAME, "email").send_keys("test22@user.com")
        self.driver.find_element(By.NAME, "password").send_keys("test**11")
        self.driver.find_element(By.NAME, "login").click()
        self.driver.back()

    def test_checkout(self):
        # Hover over first product
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h3[1]")))
        self.driver.execute_script("arguments[0].hover();", self.driver.find_element(By.XPATH, "//h3[1]"))

        # Click "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart_button.click()

        # Open popup cart
        self.driver.find_element(By.XPATH, "//a[@class='open-cart']").click()
        
        # Wait for popup to be visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cart-content")))

        # Click "View cart" button inside popup
        view_cart_button = self.driver.find_element(By.LINK_TEXT, "View cart")
        if view_cart_button.is_enabled():
            view_cart_button.click()

        # Go to cart page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h3[1][contains(text(), 'Cart')]")))

        # Click "Proceed to Checkout" button
        proceed_to_checkout_button = self.driver.find_element(By.LINK_TEXT, "Proceed to checkout")
        if proceed_to_checkout_button.is_enabled():
            proceed_to_checkout_button.click()

        # Fill out billing form
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "checkout-payment-form")))

        company_input = self.driver.find_element(By.ID, "company")
        company_input.send_keys("Comp1")

        address_input = self.driver.find_element(By.ID, "address")
        address_input.send_keys("Street1")

        city_input = self.driver.find_element(By.ID, "city")
        city_input.send_keys("Quebec")

        # Select region/state from dropdown
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "region")))
        select_region_button = self.driver.find_element(By.LINK_TEXT, "Select region")
        if select_region_button.is_enabled():
            select_region_button.click()

        region_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "region")))
        region_options = region_dropdown.find_elements(By.XPATH, ".//option")
        for option in region_options:
            if option.text == 'Québec':
                option.click()
                break

        postal_code_input = self.driver.find_element(By.ID, "postal_code")
        postal_code_input.send_keys("1234")

        phone_number_input = self.driver.find_element(By.ID, "phone")
        phone_number_input.send_keys("1234567891")

        terms_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "terms")))
        if terms_checkbox.is_enabled():
            terms_checkbox.click()

        # Wait for any maps popups or warnings and close them
        map_popup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "map-poup")))
        if map_popup:
            self.driver.execute_script("document.getElementById('map-poup').style.display='none';")

        # Confirm success
        company_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "company")))
        self.assertIsNotNone(company_input.get_attribute("value"))
        address_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "address")))
        self.assertIsNotNone(address_input.get_attribute("value"))
        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "city")))
        self.assertIsNotNone(city_input.get_attribute("value"))
        region_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "region")))
        self.assertIsNotNone(region_dropdown.get_attribute("value"))
        postal_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "postal_code")))
        self.assertIsNotNone(postal_code_input.get_attribute("value"))
        phone_number_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "phone")))
        self.assertIsNotNone(phone_number_input.get_attribute("value"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()