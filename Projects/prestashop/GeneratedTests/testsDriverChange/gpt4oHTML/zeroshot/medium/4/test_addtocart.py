import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080/en/"
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the home page.
        driver.get(self.base_url)

        # Step 2: Click on a product category (e.g. 'Clothes' from the top menu).
        category_link = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "ul#top-menu > li.category > a[href*='3-clothes']")))
        category_link.click()

        # Step 3: Select the first product listed in the category.
        first_product = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "div.js-product.product a.product-thumbnail")))
        first_product.click()

        # Step 4: On the product detail page, click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.add-to-cart")))
        add_to_cart_button.click()

        # Step 5: Wait for the modal popup that confirms the product was added to the cart.
        modal = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#blockcart-modal")))
        
        # Step 6: Verify the modal contains a message like "Product successfully added to your shopping cart".
        modal_title = modal.find_element(By.XPATH, ".//h4[contains(@class,'modal-title')]")
        if not modal_title or "successfully added to your shopping cart" not in modal_title.text:
            self.fail("Success message not found in modal")

if __name__ == "__main__":
    unittest.main()