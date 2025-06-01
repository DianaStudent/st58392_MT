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
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category from the top navigation menu (e.g. ART).
        art_category_link = wait.until(EC.presence_of_element_located((By.ID, "category-9")))
        if art_category_link:
            art_category_link.click()
        else:
            self.fail("Art category link not found.")

        # 3. Wait for the category page to load.
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list-header")))

        # 4. Click on the first product in the list.
        first_product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']/div/div[1]//a[@class='thumbnail product-thumbnail']")))
        if first_product_link:
            first_product_link.click()
        else:
            self.fail("First product link not found.")

        # 5. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 6. Wait for the modal popup to appear after the product is added.
        modal = wait.until(EC.presence_of_element_located((By.ID, "blockcart-modal")))

        # 7. Confirm that the modal title or content includes a success message like "successfully added".
        if modal:
            modal_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-header .modal-title")))
            if modal_title and modal_title.text:
                self.assertTrue("successfully added" in modal_title.text.lower(), "Success message not found in modal title.")
            else:
                self.fail("Modal title not found or is empty.")
        else:
            self.fail("Modal popup not found after adding to cart.")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to checkout")))
        if proceed_to_checkout_button:
            self.assertTrue(proceed_to_checkout_button.is_displayed(), "Proceed to checkout button is not displayed.")
        else:
            self.fail("Proceed to checkout button not found.")


if __name__ == "__main__":
    unittest.main()