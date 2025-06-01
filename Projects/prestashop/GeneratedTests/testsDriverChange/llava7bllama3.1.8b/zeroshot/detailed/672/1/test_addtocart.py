from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_to_cart(self):
        self.driver.get("http://localhost:8080/en/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "topnav")))
        
        # Click on a product category from the top navigation menu
        category = self.driver.find_element_by_link_text("ART")
        ActionChains(self.driver).move_to_element(category).perform()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@id='submenu']//a[text()='Artworks']")))
        
        # Wait for the category page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "product-list")))
        
        # Click on the first product in the list
        first_product = self.driver.find_elements_by_class_name("item")[0]
        first_product.click()
        
        # Wait for the modal popup to appear after the product is added
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cart']//button[text()='Proceed to checkout']")))
        
        # Confirm that the modal title or content includes a success message like "successfully added"
        self.assertIn("Successfully added", self.driver.find_element_by_xpath("//h2").text)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()