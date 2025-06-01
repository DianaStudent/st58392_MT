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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category from the top navigation menu (e.g. ART).
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "category-9"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not click on Art category link: {e}")

        # 3. Wait for the category page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "js-product-list-header"))
            )
        except Exception as e:
            self.fail(f"Art category page did not load correctly: {e}")

        # 4. Click on the first product in the list.
        try:
            first_product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//article[@class='product-miniature js-product-miniature reviews-loaded'][1]//a[@class='thumbnail product-thumbnail']"))
            )
            first_product_link.click()
        except Exception as e:
            self.fail(f"Could not click on the first product: {e}")

        # 5. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on Add to cart button: {e}")

        # 6. Wait for the modal popup to appear after the product is added.
        try:
            modal = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal popup did not appear: {e}")

        # 7. Confirm that the modal title or content includes a success message like "successfully added".
        try:
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "myModalLabel"))
            )
            if modal_title.text:
                self.assertTrue("successfully added" in modal_title.text,
                                f"Modal title does not contain 'successfully added'. Actual title: {modal_title.text}")
            else:
                self.fail("Modal title is empty.")
        except Exception as e:
            self.fail(f"Could not verify modal title: {e}")

        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='cart-content-btn']/a[@class='btn btn-primary']"))
            )
            self.assertTrue(checkout_button.is_displayed(), "Proceed to checkout button is not displayed")
        except Exception as e:
            self.fail(f"Could not locate or verify Proceed to checkout button: {e}")


if __name__ == "__main__":
    unittest.main()