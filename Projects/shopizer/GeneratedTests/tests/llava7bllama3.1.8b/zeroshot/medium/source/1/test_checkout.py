import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from webdriver_manager.chrome import ChromeDriverManager
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        self.email_input = self.driver.find_element(By.ID, "email")
        self.password_input = self.driver.find_element(By.ID, "password")

    def tearDown(self):
        pass

    def test_checkout(self):
        # Login
        self.email_input.send_keys("test22@user.com")
        self.password_input.send_keys("test**11")
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()

        # Add product to cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
        add_to_cart_button.click()

        # Go to cart and proceed to checkout
        view_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']")))
        view_cart_button.click()
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "proceed-to-checkout")))
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "first_name")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "last_name")))
        address_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "address")))
        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "city")))
        region_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.NAME, "region")))
        postal_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "postal_code")))
        country_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "country")))

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        address_input.send_keys("123 Main St")
        city_input.send_keys("New York")
        region_input.send_keys("NY")  # Wait for the region field to appear dynamically
        postal_code_input.send_keys("10001")
        country_select.click()

        accept_terms_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accept_terms']")))
        accept_terms_button.click()

        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "place-order")))
        self.assertEqual(first_name_input.get_attribute("value"), "John")
        self.assertEqual(last_name_input.get_attribute("value"), "Doe")
        self.assertEqual(address_input.get_attribute("value"), "123 Main St")
        self.assertEqual(city_input.get_attribute("value"), "New York")
        self.assertEqual(region_input.get_attribute("value"), "NY")
        self.assertEqual(postal_code_input.get_attribute("value"), "10001")

if __name__ == "__main__":
    unittest.main()