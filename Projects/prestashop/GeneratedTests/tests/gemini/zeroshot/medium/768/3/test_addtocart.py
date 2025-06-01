import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category (e.g. from the top menu).
        try:
            category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "category-9"))
            )
            category_link.click()
        except Exception as e:
            self.fail(f"Could not click on category link: {e}")

        # 3. Select the first product listed in the category.
        try:
            first_product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='js-product-list']/div/div[1]//a[@class='thumbnail product-thumbnail']"))
            )
            first_product_link.click()
        except Exception as e:
            self.fail(f"Could not click on first product link: {e}")

        # 4. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on add to cart button: {e}")

        # 5. Wait for the modal popup that confirms the product was added to the cart.
        try:
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal did not appear: {e}")

        # 6. Verify the modal contains a message like "Product successfully added to your shopping cart".
        try:
            modal_title_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-title"))
            )
            modal_title = modal_title_element.text
            self.assertIn("successfully added", modal_title)
        except Exception as e:
            self.fail(f"Could not verify modal title: {e}")

if __name__ == "__main__":
    unittest.main()