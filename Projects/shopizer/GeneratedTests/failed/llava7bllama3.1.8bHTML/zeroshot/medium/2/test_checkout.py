from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_shopping_cart(self):
        # 1. Open the home page.
        self.driver.get("http://localhost/")

        # 2. Log in using the provided credentials.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("test22@user.com")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("test**11")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "loginbtn"))).click()

        # 3. Add product to the cart.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Product 1"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart-button"))).click()

        # 4. Open the cart and navigate to the cart page.
        self.driver.get("http://localhost/cart")

        # 5. Click "Proceed to Checkout".
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))).click()

        # 6. Fill in the billing form.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_first_name"))).send_keys("John")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_last_name"))).send_keys("Doe")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_company"))).send_keys("ABC Company")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_address_1"))).send_keys("123 Main St")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_city"))).send_keys("New York")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_postcode"))).send_keys("10001")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "option_0"))).click() # Select state
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("test22@user.com")

        # 7. Accept terms and proceed.
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()

        # 8. Confirm success if form is filled.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "billing_first_name"))).get_attribute("value") != ""

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()