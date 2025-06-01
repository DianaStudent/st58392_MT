import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        # Open home page
        self.driver.get("http://localhost:3000/")

        # Click on product category (e.g. Category A)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category/a']"))).click()

        # Select the first product (e.g. Product A)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/product/1']"))).click()

        # Click the "Add to cart" button
        self.driver.find_element(By.XPATH, "//button[@class='add-to-cart']").click()

        # Explicitly click the cart icon (shopping bag)
        self.driver.find_element(By.XPATH, "//img[@class='cart-button']").click()

        # Wait for presence of "GO TO CHECKOUT" button using html_data
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@text()='GO TO CHECKOUT']")))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()