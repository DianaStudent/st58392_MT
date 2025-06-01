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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the "Art" category from the top navigation menu.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category-9"))
        )
        if art_category_link:
            art_category_link.click()
        else:
            self.fail("Art category link not found.")

        # 3. Wait for the category page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "js-product-list-header"))
        )

        # 4. Click on the first product in the list.
        first_product_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product .product-thumbnail"))
        )
        if first_product_link:
            first_product_link.click()
        else:
            self.fail("First product link not found.")

        # 5. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 6. Wait for the modal popup to appear after the product is added.
        modal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # 7. Confirm that the modal title or content includes a success message like "successfully added".
        modal_title_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-title"))
        )

        if modal_title_element:
            modal_title = modal_title_element.text
            if modal_title and "successfully added" in modal_title:
                pass  # Success message found
            else:
                self.fail("Success message not found in modal title.")
        else:
            self.fail("Modal title element not found.")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to checkout"))
        )
        if not proceed_to_checkout_button:
            self.fail("Proceed to checkout button not found in modal.")

if __name__ == "__main__":
    unittest.main()