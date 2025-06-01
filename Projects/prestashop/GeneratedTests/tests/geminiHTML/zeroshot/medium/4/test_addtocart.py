import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category (e.g. from the top menu).
        category_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a")))
        if category_link:
            category_link.click()
        else:
            self.fail("Category link not found.")

        # 3. Select the first product listed in the category.
        first_product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[1]//a[@class='thumbnail product-thumbnail']")))
        if first_product_link:
            first_product_link.click()
        else:
            self.fail("First product link not found.")

        # 4. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Wait for the modal popup that confirms the product was added to the cart.
        modal = wait.until(EC.visibility_of_element_located((By.ID, "blockcart-modal")))

        # 6. Verify the modal contains a message like "Product successfully added to your shopping cart".
        if modal:
            modal_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-header .modal-title")))
            if modal_title_element:
                modal_title_text = modal_title_element.text
                if "Product successfully added to your shopping cart" in modal_title_text:
                    pass  # Success!
                else:
                    self.fail(f"Modal title text is incorrect. Expected 'Product successfully added to your shopping cart', but got: '{modal_title_text}'")
            else:
                self.fail("Modal title element not found.")
        else:
            self.fail("Modal popup not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()