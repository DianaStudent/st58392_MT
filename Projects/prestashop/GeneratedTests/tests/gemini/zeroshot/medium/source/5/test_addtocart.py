import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category (e.g. from the top menu).
        category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a"))
        )
        if category_link:
            category_link.click()
        else:
            self.fail("Category link not found")

        # 3. Select the first product listed in the category.
        first_product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[1]//a[@class='thumbnail product-thumbnail']"))
        )
        if first_product_link:
            first_product_link.click()
        else:
            self.fail("First product link not found")

        # 4. On the product detail page, click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 5. Wait for the modal popup that confirms the product was added to the cart.
        modal = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "blockcart-modal"))
        )
        if not modal:
            self.fail("Modal not found")

        # 6. Verify the modal contains a message like "Product successfully added to your shopping cart".
        modal_title_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']/div[@class='modal-header']/h4[@class='modal-title h6 text-sm-center']"))
        )

        if modal_title_element:
            modal_title_text = modal_title_element.text
            self.assertIn("Product successfully added to your shopping cart", modal_title_text)
        else:
            self.fail("Modal title not found")

if __name__ == "__main__":
    unittest.main()