import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode for tests
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")
        
        # Step 2: Navigate to 'Art' category
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Art']")))
        art_category_link.click()
        
        # Step 3: Click on a product from 'Art' category
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'The best is yet to come')]")))
        product_link.click()
        
        # Step 4: Click the 'Add to cart' button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'add-to-cart') and contains(@class, 'btn-primary')]")))
        add_to_cart_button.click()
        
        # Step 5: Wait for the confirmation modal to appear and verify the success message
        modal_title = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(@class, 'modal-title')]")))
        self.assertIn("successfully added", modal_title.text.lower(), "Modal title does not indicate success.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()