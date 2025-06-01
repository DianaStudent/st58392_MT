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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = "http://localhost:8080/en/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Click on a product category from the top navigation menu (e.g. ART).
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "category-9"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not click on Art category link: {e}")

        # 2. Click on the first product in the list.
        try:
            first_product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//article[1]//a"))
            )
            first_product_link.click()
        except Exception as e:
            self.fail(f"Could not click on the first product: {e}")

        # 3. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on Add to cart button: {e}")

        # 4. Wait for the modal popup to appear after the product is added.
        try:
            modal_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal did not appear: {e}")

        # 5. Confirm that the modal title or content includes a success message like "successfully added".
        try:
            modal_title_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-title"))
            )
            modal_title_text = modal_title_element.text
            self.assertIn("successfully added", modal_title_text, "Success message not found in modal title")
        except Exception as e:
            self.fail(f"Could not verify success message in modal title: {e}")

        # 6. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        try:
            proceed_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to checkout"))
            )
            self.assertTrue(proceed_to_checkout_button.is_displayed(), "Proceed to checkout button is not displayed")
        except Exception as e:
            self.fail(f"Could not find Proceed to checkout button: {e}")

if __name__ == "__main__":
    unittest.main()