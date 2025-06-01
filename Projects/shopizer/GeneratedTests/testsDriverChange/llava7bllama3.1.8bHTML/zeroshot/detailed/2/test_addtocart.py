import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_cart(self):
        # Open the home page
        self.driver.get("http://localhost/")

        # Hover over the first product
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-list']//a[1]"))
        ).location_once_scrolled_into_view
        self.driver.execute_script("arguments[0].style.opacity = '1';", self.driver.find_element(By.XPATH, "//div[@class='product-list']//a[1]"))

        # Click the revealed "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='add-to-cart-btn']"))
        ).click()

        # Click the cart icon to open the popup cart
        self.driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

        # Wait for the popup to become visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='popup-cart']"))
        )

        # Click "View cart" or similar button inside the popup
        self.driver.find_element(By.XPATH, "//button[@class='view-cart-btn']").click()

        # On the cart page, verify that the product appears in the cart list
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='cart-list']//tr[1]"))
        )
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//table[@class='cart-list']//tr[1]/td[2]"))

if __name__ == "__main__":
    unittest.main()