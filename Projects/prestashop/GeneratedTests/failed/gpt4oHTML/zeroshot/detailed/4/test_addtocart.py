from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the "Art" category from the top navigation menu.
        art_category_selector = (By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")
        art_category = wait.until(EC.presence_of_element_located(art_category_selector))
        art_category.click()

        # Step 3: Wait for the category page to load.
        wait.until(EC.presence_of_element_located((By.ID, "category")))

        # Step 4: Click on the first product in the list.
        first_product_selector = (By.CSS_SELECTOR, ".js-product-miniature .product-description a")
        first_product = wait.until(EC.presence_of_element_located(first_product_selector))
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button.
        add_to_cart_selector = (By.CSS_SELECTOR, "button.add-to-cart")
        add_to_cart_button = wait.until(EC.element_to_be_clickable(add_to_cart_selector))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear.
        modal_selector = (By.ID, "blockcart-modal")
        wait.until(EC.visibility_of_element_located(modal_selector))

        # Step 7: Confirm that the modal title or content includes a success message.
        modal_title_selector = (By.CSS_SELECTOR, "#blockcart-modal .modal-title")
        modal_title = wait.until(EC.presence_of_element_located(modal_title_selector))
        if not modal_title or "successfully added" not in modal_title.text.lower():
            self.fail("The success message is not displayed in the modal title.")

        # Step 8: Assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_selector = (By.LINK_TEXT, "Proceed to checkout")
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable(proceed_to_checkout_selector))
        if not proceed_to_checkout_button:
            self.fail("The 'Proceed to checkout' button is missing in the modal.")

if __name__ == "__main__":
    unittest.main()