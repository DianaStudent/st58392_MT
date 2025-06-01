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

        # 1. Click on a product category (e.g. from the top menu).
        category_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a"))
        )
        category_link.click()

        # 2. Select the first product listed in the category.
        first_product_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[1]//a[@class='thumbnail product-thumbnail']"))
        )
        first_product_link.click()

        # 3. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
        )
        add_to_cart_button.click()

        # 4. Wait for the modal popup that confirms the product was added to the cart.
        modal = wait.until(
            EC.visibility_of_element_located((By.ID, "blockcart-modal"))
        )

        # 5. Verify the modal contains a message like "Product successfully added to your shopping cart".
        modal_title_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-header']/h4[@class='modal-title h6 text-sm-center']"))
        )

        if modal_title_element:
            modal_title_text = modal_title_element.text
            if modal_title_text:
                self.assertTrue("Product successfully added to your shopping cart" in modal_title_text,
                                "Modal title does not contain expected message.")
            else:
                self.fail("Modal title text is empty.")
        else:
            self.fail("Modal title element not found.")

if __name__ == "__main__":
    unittest.main()