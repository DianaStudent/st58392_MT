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

        # 1. Open the home page.
        self.assertEqual(driver.current_url, self.url)

        # 2. Click on a product category from the top navigation menu (e.g. ART).
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
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product .product-title a"))
        )
        if first_product_link:
            first_product_link.click()
        else:
            self.fail("First product link not found.")

        # 5. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
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
        if modal:
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-title"))
            )
            if modal_title and modal_title.text:
                self.assertTrue("successfully added" in modal_title.text.lower(), "Success message not found in modal title.")
            else:
                self.fail("Modal title not found or is empty.")
        else:
            self.fail("Modal popup not found after adding to cart.")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Proceed to checkout"))
        )
        if not proceed_to_checkout_button:
            self.fail("Proceed to checkout button not found in modal.")

if __name__ == "__main__":
    unittest.main()