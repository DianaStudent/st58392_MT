from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://localhost/checkout")

    def test_checkout_process(self):
        # Login
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("test22@user.com")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("test11")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Add products to cart
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product1']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']"))).click()

        # Go to cart page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']"))).click()

        # Click "Proceed to Checkout"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()

        # Fill in the billing form
        self.driver.find_element(By.ID, "email").send_keys("test22@user.com")
        self.driver.find_element(By.ID, "password").send_keys("test11")

        # Confirm success by verifying that the billing form is filled
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
            self.fail("Billing form should be filled in")
        except TimeoutException:
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()