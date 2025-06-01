import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        
        # Step 2: Click on a product category, e.g., ART
        art_category_selector = (By.CSS_SELECTOR, 'a[href*="/9-art"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(art_category_selector)).click()
        
        # Step 3: Wait for the category page to load
        product_list_selector = (By.ID, 'js-product-list')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_list_selector))
        
        # Step 4: Click on the first product in the list
        first_product_selector = (By.CSS_SELECTOR, '.product a.product-thumbnail')
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(first_product_selector))[0].click()
        
        # Step 5: Click the "Add to cart" button on the product detail page
        add_to_cart_button_selector = (By.CSS_SELECTOR, 'button.add-to-cart')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(add_to_cart_button_selector)).click()
        
        # Step 6: Wait for the modal popup to appear
        modal_selector = (By.ID, 'blockcart-modal')
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(modal_selector))
        
        # Step 7: Confirm that the modal title or content includes a success message
        modal_title_selector = (By.CSS_SELECTOR, '.modal-title.h6.text-sm-center')
        modal_title = WebDriverWait(driver, 20).until(EC.presence_of_element_located(modal_title_selector))
        
        if modal_title and "successfully added" in modal_title.text:
            # Step 8: Assert the presence of a "Proceed to checkout" button
            proceed_to_checkout_selector = (By.CSS_SELECTOR, 'a[href*="cart?action=show"]')
            proceed_to_checkout = WebDriverWait(driver, 20).until(EC.presence_of_element_located(proceed_to_checkout_selector))
            
            if not proceed_to_checkout:
                self.fail("Proceed to checkout button not found in the cart modal.")
        else:
            self.fail("Success message not found in modal title.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()