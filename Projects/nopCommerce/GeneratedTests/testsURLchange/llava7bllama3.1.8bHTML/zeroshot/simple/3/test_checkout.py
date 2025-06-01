import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestOrderCompletion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_order_completion(self):
        # Open the webpage
        self.driver.get("http://max/")

        # Find product and add to cart
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for products']"))
        ).send_keys("book")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Shopping Cart"))
        ).click()

        # Use the "Checkout as Guest" option
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "checkout_as_guest_link"))
        ).click()

        # Fill in guest checkout form
        self.driver.find_element(By.XPATH, "//input[@name='FirstName']").send_keys("Test")
        self.driver.find_element(By.XPATH, "//input[@name='LastName']").send_keys("User")
        self.driver.find_element(By.XPATH, "//input[@name='Email']").send_keys("random_email")
        self.driver.find_element(By.XPATH, "//input[@name='City']").send_keys("Riga")
        self.driver.find_element(By.XPATH, "//input[@name='Address1']").send_keys("Street 1")
        self.driver.find_element(By.XPATH, "//input[@name='ZipPostalCode']").send_keys("LV-1234")
        self.driver.find_element(By.XPATH, "//input[@name='PhoneNumber']").send_keys("12345678")

        # Select shipping and payment options
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "shippingoption_1"))
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        ).click()

        # Fill in credit card details
        self.driver.find_element(By.XPATH, "//input[@name='CreditCardType']").send_keys("visa")
        self.driver.find_element(By.XPATH, "//input[@name='CardholderName']").send_keys("Test User")
        self.driver.find_element(By.XPATH, "//input[@name='CardNumber']").send_keys("4111111111111111")
        self.driver.find_element(By.XPATH, "//input[@name='ExpireMonth']").send_keys("4")
        self.driver.find_element(By.XPATH, "//input[@name='ExpireYear']").send_keys("2027")
        self.driver.find_element(By.XPATH, "//input[@name='CardCode']").send_keys("123")

        # Confirm order
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "confirm-order-next-step-button"))
        ).click()

        # Check for order completion message
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']"))
        )

    def test_order_completed_page(self):
        self.driver.get("http://max/")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//strong[text()='Order number: 7']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Click here for order details."))
        )

if __name__ == "__main__":
    unittest.main()