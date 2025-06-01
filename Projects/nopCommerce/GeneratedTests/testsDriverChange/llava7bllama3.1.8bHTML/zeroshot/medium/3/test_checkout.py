from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestOrderProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_order_process(self):
        # Click on the "Search" link and search for a product (e.g. "book")
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='q']")))
        search_input.send_keys("book")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Click the "Add to cart" button for the first item in the search results
        product_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Add to Cart')])[1]")))
        product_button.click()

        # Open the shopping cart via the success notification popup
        cart_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='success-notification']//a[text()='Shopping Cart']")))
        cart_link.click()

        # Accept terms of service and click the "Checkout" button
        self.driver.find_element(By.XPATH, "(//input[@name='accept-terms-of-service'])[1]").click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Choose "Checkout as Guest"
        self.driver.find_element(By.XPATH, "//a[text()='Checkout as Guest']").click()

        # Fill in the billing address
        fields = ["FirstName", "LastName", "Email", "City", "Address1", "ZipPostalCode", "PhoneNumber", "CountryId"]
        for field in fields:
            if not self.driver.find_element(By.XPATH, f"//input[@name='{field}']").get_attribute("value"):
                self.driver.find_element(By.XPATH, f"//input[@name='{field}']").send_keys(getattr(self, f"{field.lower()}"))

        # Select shipping and payment methods
        self.driver.find_element(By.XPATH, "//label[text()='Shipping Option']/preceding-sibling::input").click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "shippingoption_1"))).click()
        self.driver.find_element(By.XPATH, "//label[text()='Payment Method Option']/preceding-sibling::input").click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "paymentmethod_1"))).click()

        # Enter credit card details
        self.driver.find_element(By.XPATH, "//input[@name='CreditCardType']").send_keys("visa")
        self.driver.find_element(By.XPATH, "//input[@name='CardholderName']").send_keys("Test User")
        self.driver.find_element(By.XPATH, "//input[@name='CardNumber']").send_keys("4111111111111111")
        self.driver.find_element(By.XPATH, "//input[@name='ExpireMonth']").send_keys("4")
        self.driver.find_element(By.XPATH, "//input[@name='ExpireYear']").send_keys("2027")
        self.driver.find_element(By.XPATH, "//input[@name='CardCode']").send_keys("123")

        # Confirm the order
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "confirm-order"))).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()