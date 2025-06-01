import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")
        
        # Step 2: Click on a product category (e.g., 'Art' from the top menu)
        art_category_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='category-9']/a"))
        )
        art_category_link.click()
        
        # Step 3: Select the first product listed in the category
        first_product_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//a[@class='thumbnail product-thumbnail']"))
        )
        first_product_link.click()
        
        # Step 4: On the product detail page, click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
        )
        add_to_cart_button.click()
        
        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        modal = self.wait.until(
            EC.visibility_of_element_located((By.ID, "blockcart-modal"))
        )
        
        # Step 6: Verify the modal contains a message like "Product successfully added to your shopping cart"
        modal_title = modal.find_element(By.XPATH, ".//h4[@class='modal-title h6 text-sm-center']")
        self.assertTrue("successfully added" in modal_title.text, "Modal title does not indicate successful addition to cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()