from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless Chrome
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Navigate to Art category
        art_category_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
        art_category_link.click()
        
        # Click on a product in the Art category
        product_link = wait.until(EC.element_to_be_clickable(
            (By.PARTIAL_LINK_TEXT, "The best is yet to come'"))
        )
        product_link.click()
        
        # Click 'Add to Cart' button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart")))
        add_to_cart_button.click()
        
        # Wait for the modal and check the success message
        modal_title = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='blockcart-modal']//h4[contains(text(), 'successfully added to your shopping cart')]"))
        )

        if not modal_title:
            self.fail("Success modal after adding to cart did not appear or had incorrect content.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()