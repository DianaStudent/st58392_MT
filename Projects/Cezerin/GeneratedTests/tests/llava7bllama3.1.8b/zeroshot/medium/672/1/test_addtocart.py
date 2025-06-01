import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        self.driver.get("http://localhost:3000/")
        
        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category1']"))).click()
        
        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product1']"))).click()
        
        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']"))).click()
        
        # Click the cart icon/button to open the shopping bag
        self.driver.find_element(By.CSS_SELECTOR, ".cart-button").click()
        
        # Wait for presence of "GO TO CHECKOUT" button
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']")))
        except TimeoutException:
            self.fail("Element not found")

if __name__ == "__main__":
    unittest.main()