import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category (e.g. from the top menu).
        category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category-9"))
        )
        if category_link:
            category_link.click()
        else:
            self.fail("Category 'Art' link not found.")

        # 3. Select the first product listed in the category.
        first_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product a.product-thumbnail"))
        )
        if first_product:
            first_product.click()
        else:
            self.fail("First product link not found.")

        # 4. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Wait for the modal popup that confirms the product was added to the cart.
        modal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # 6. Verify the modal contains a message like "Product successfully added to your shopping cart".
        if modal:
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-title"))
            )
            if modal_title:
                modal_title_text = modal_title.text
                if modal_title_text:
                    self.assertIn("Product successfully added to your shopping cart", modal_title_text)
                else:
                    self.fail("Modal title text is empty.")
            else:
                self.fail("Modal title element not found.")
        else:
            self.fail("Modal popup not found after adding to cart.")

if __name__ == "__main__":
    unittest.main()