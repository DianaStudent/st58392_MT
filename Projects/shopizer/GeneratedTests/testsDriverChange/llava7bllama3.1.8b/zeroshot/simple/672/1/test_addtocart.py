import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_add_to_cart_and_view_cart(self):
        self.driver.get("http://localhost/")
        
        # Hover over a product item to reveal the "Add to cart" button
        product_item = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-item']")))
        product_item.find_element(By.TAG_NAME, "h2").click()
        
        # Open the cart popup by clicking the cart icon
        cart_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='cart-icon']")))
        cart_icon.click()
        
        # Confirm success by checking that the popup contains at least one item
        cart_popup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-popup']")))
        self.assertGreater(len(cart_popup.find_elements(By.TAG_NAME, "li")), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()