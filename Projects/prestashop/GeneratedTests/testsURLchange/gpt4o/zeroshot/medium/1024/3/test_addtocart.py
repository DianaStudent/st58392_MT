import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")

        # Step 2: Click on a product category (e.g. 'Art' category from the top menu)
        category_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        if not category_link:
            self.fail("Category link not found.")
        category_link.click()

        # Step 3: Select the first product listed in the category
        first_product = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='products row']//h2/a"))
        )
        if not first_product:
            self.fail("First product not found.")
        first_product.click()

        # Step 4: On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart"))
        )
        if not add_to_cart_button:
            self.fail("Add to Cart button not found.")
        add_to_cart_button.click()

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        modal = wait.until(
            EC.visibility_of_element_located((By.ID, "blockcart-modal"))
        )
        if not modal:
            self.fail("Add to Cart confirmation modal not displayed.")

        # Step 6: Verify the modal contains a message like "Product successfully added to your shopping cart"
        modal_title = modal.find_element(By.CLASS_NAME, "modal-title")
        if not modal_title or "successfully added" not in modal_title.text.lower():
            self.fail("Success message not found in modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()