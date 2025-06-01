import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_flow(self):
        # Login
        login_email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        login_email_input.send_keys("test22@user.com")

        login_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login_password_input.send_keys("test**11")

        self.driver.find_element(By.TAG_NAME, "button").click()

        # Navigate back to home page
        self.driver.get("http://localhost/")

        # Hover over the first product and click add to cart
        product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "product-list"))
        )

        product_link = WebDriverWait(product_list, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-name='Product 1']"))
        )
        product_link.click()

        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Open popup cart and click view cart
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-name='cart']"))
        )

        cart_icon.click()
        self.driver.find_element(By.ID, "view-cart-button").click()

        # Proceed to checkout and fill billing form
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-name='proceed-to-checkout']"))
        )
        proceed_to_checkout_button.click()

        company_input = self.driver.find_element(By.ID, "company")
        company_input.send_keys("Comp1")

        address_input = self.driver.find_element(By.ID, "address")
        address_input.send_keys("Street1")

        city_input = self.driver.find_element(By.ID, "city")
        city_input.send_keys("Quebec")

        region_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "region"))
        )
        region_input.click()
        region_label = WebDriverWait(region_input, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[@for='region']"))
        )
        self.assertEqual("Select Region", region_label.text)

        # Simulate select option
        region_input.send_keys("Ontario")

        postal_code_input = self.driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys("1234")

        phone_number_input = self.driver.find_element(By.ID, "phone-number")
        phone_number_input.send_keys("1234567891")

        terms_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='terms']"))
        )
        terms_checkbox.click()

        # Wait for any maps popups or warnings and close them
        self.driver.find_elements(By.TAG_NAME, "button")[-1].click()  # Close warning

        # Confirm success by verifying that the billing form is filled
        company_value = self.driver.find_element(By.ID, "company").get_attribute("value")
        address_value = self.driver.find_element(By.ID, "address").get_attribute("value")
        city_value = self.driver.find_element(By.ID, "city").get_attribute("value")
        region_value = self.driver.find_element(By.ID, "region").get_attribute("value")
        postal_code_value = self.driver.find_element(By.ID, "postal-code").get_attribute("value")
        phone_number_value = self.driver.find_element(By.ID, "phone-number").get_attribute("value")

        self.assertEqual(company_value, "Comp1")
        self.assertEqual(address_value, "Street1")
        self.assertEqual(city_value, "Quebec")
        self.assertEqual(region_value, "Ontario")  # Simulated select option
        self.assertEqual(postal_code_value, "1234")
        self.assertEqual(phone_number_value, "1234567891")

if __name__ == "__main__":
    unittest.main()