import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get("http://localhost:8080")  # Assuming `localhost:8080` is the correct URL
        self.wait = WebDriverWait(self.browser, 20)

    def tearDown(self):
        self.browser.quit()

    def test_add_to_cart_process(self):
        # Accept cookies if the button is present
        try:
            cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        product_wrap = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        
        # Use ActionChains to hover and click the 'Add to cart' button
        ActionChains(self.browser).move_to_element(product_wrap).click(add_to_cart_button).perform()

        # Open cart popup by clicking the cart icon
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon.click()

        # Confirm success by checking that the popup contains at least one item
        try:
            cart_popup = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
            )
            items_in_cart = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            if not items_in_cart:
                self.fail("Cart popup does not contain any items.")
        except:
            self.fail("Could not open the cart popup or find items.")

if __name__ == "__main__":
    unittest.main()