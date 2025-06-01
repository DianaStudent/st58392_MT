import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_to_cart(self):
        self.driver.get("http://localhost:3000/")

        # Click on the product to add it to cart
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/addtocart-simple']"))
        ).click()

        # Wait for presence of "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']"))
        )

    def test_cart_button_presence(self):
        self.driver.get("http://localhost:3000/")

        # Click on the product to add it to cart
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/addtocart-simple']"))
        ).click()

        # Wait for presence of "GO TO CHECKOUT" button and its parent div (cart)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//button[text()='GO TO CHECKOUT'])[1]/../../../.."))
        )

if __name__ == "__main__":
    unittest.main()