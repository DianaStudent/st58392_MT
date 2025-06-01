import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_product_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page (already done in setUp)

        # 2. Click on the "Art" category from the top navigation menu.
        try:
            art_category_link = wait.until(
                EC.presence_of_element_located((By.ID, "category-9"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not click Art category link: {e}")

        # 3. Wait for the category page to load.
        try:
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "products-selection"))
            )
        except Exception as e:
            self.fail(f"Category page did not load correctly: {e}")

        # 4. Click on the first product in the list.
        try:
            first_product_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product a.product-thumbnail"))
            )
            first_product_link.click()
        except Exception as e:
            self.fail(f"Could not click the first product link: {e}")

        # 5. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click the Add to cart button: {e}")

        # 6. Wait for the modal popup to appear after the product is added.
        try:
            wait.until(
                EC.presence_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal popup did not appear: {e}")

        # 7. Confirm that the modal title includes a success message like "successfully added".
        try:
            modal_title_element = wait.until(
                EC.presence_of_element_located((By.ID, "myModalLabel"))
            )
            modal_title_text = modal_title_element.text
            self.assertIn("successfully added", modal_title_text, "Modal title does not contain success message.")
        except Exception as e:
            self.fail(f"Could not verify modal title: {e}")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        try:
            proceed_to_checkout_button = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Proceed to checkout"))
            )
            self.assertTrue(proceed_to_checkout_button.is_displayed(), "Proceed to checkout button is not displayed.")
        except Exception as e:
            self.fail(f"Could not verify Proceed to checkout button: {e}")

if __name__ == "__main__":
    unittest.main()