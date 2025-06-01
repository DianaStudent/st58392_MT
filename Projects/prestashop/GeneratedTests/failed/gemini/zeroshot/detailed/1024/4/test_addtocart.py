from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category from the top navigation menu (e.g. ART).
        try:
            art_category_link = wait.until(
                EC.presence_of_element_located((By.ID, "category-9"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not click on Art category link: {e}")

        # 3. Wait for the category page to load.
        try:
            wait.until(
                EC.presence_of_element_located((By.ID, "js-product-list-header"))
            )
        except Exception as e:
            self.fail(f"Art category page did not load correctly: {e}")

        # 4. Click on the first product in the list.
        try:
            first_product_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//article[@class='product-miniature js-product-miniature reviews-loaded'][1]//a[@class='thumbnail product-thumbnail']"))
            )
            first_product_link.click()
        except Exception as e:
            self.fail(f"Could not click on the first product: {e}")

        # 5. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on Add to cart button: {e}")

        # 6. Wait for the modal popup to appear after the product is added.
        try:
            wait.until(
                EC.presence_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal popup did not appear: {e}")

        # 7. Confirm that the modal title or content includes a success message like "successfully added".
        try:
            modal_title = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-title"))
            )
            modal_title_text = modal_title.text
            self.assertIn("successfully added", modal_title_text, "Success message is not present in the modal title")
        except Exception as e:
            self.fail(f"Could not verify success message in modal: {e}")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        try:
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to checkout"))
            )
            self.assertTrue(checkout_button.is_displayed(), "Proceed to checkout button is not displayed")
        except Exception as e:
            self.fail(f"Could not find or verify Proceed to checkout button: {e}")


if __name__ == "__main__":
    unittest.main()