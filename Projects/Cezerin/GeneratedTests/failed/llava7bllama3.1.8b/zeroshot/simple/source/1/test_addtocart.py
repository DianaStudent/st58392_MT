from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')

    def test_add_to_cart(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-image']"))
        )

        # Click on Add to Cart button
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
        add_to_cart_button.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//a[text()='GO TO CHECKOUT'])[1]"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()