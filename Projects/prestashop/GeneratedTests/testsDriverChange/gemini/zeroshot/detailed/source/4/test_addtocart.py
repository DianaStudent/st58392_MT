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
        art_category_link = wait.until(
            EC.presence_of_element_located((By.ID, "category-9"))
        )
        art_category_link.click()

        # 3. Wait for the category page to load.
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-category"))
        )

        # 4. Click on the first product in the list.
        first_product_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product .product-title a"))
        )
        first_product_link.click()

        # 5. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
        )
        add_to_cart_button.click()

        # 6. Wait for the modal popup to appear after the product is added.
        modal = wait.until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # 7. Confirm that the modal title or content includes a success message like "successfully added".
        modal_title_element = wait.until(
            EC.presence_of_element_located((By.ID, "myModalLabel"))
        )
        modal_title = modal_title_element.text

        if not modal_title:
            self.fail("Modal title is missing.")

        if "successfully added" not in modal_title.lower():
            self.fail(f"Modal title does not contain 'successfully added'. Actual title: {modal_title}")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Proceed to checkout"))
        )
        self.assertTrue(proceed_to_checkout_button.is_displayed(), "Proceed to checkout button is not displayed.")


if __name__ == "__main__":
    unittest.main()