import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        driver.get('http://localhost:8080/en/')

        # Click on a product category from the top navigation menu (e.g. ART)
        category_menu = wait.until(
            EC.presence_of_element_located((By.ID, 'category-9'))
        )
        category_menu.find_element(By.TAG_NAME, 'a').click()

        # Wait for the category page to load and click on the first product in the list
        first_product = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.js-product a.thumbnail'))
        )
        first_product.click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart'))
        )
        add_to_cart_button.click()

        # Wait for the modal popup to appear after the product is added
        modal = wait.until(
            EC.presence_of_element_located((By.ID, 'blockcart-modal'))
        )

        # Confirm that the modal title or content includes a success message like "successfully added"
        modal_title = modal.find_element(By.CLASS_NAME, 'modal-title')
        if not modal_title or "successfully added" not in modal_title.text:
            self.fail("The success message was not found in the modal title.")

        # Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = modal.find_element(By.XPATH, "//a[contains(@class,'btn btn-primary')]")
        if not proceed_to_checkout_button:
            self.fail("Proceed to checkout button is missing in the modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()