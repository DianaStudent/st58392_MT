import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('http://localhost/')  # Assuming the base URL is a localhost
        
    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 2. Hover over the first product.
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img")))
        ActionChains(driver).move_to_element(first_product).perform()

        # 3. Click the revealed "Add to cart" button.
        add_to_cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_button.click()

        # 4. Click the cart icon to open the popup cart.
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # 5. Wait for the popup to become visible.
        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Assert the cart popup contains at least one item.
        self.assertTrue(cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart"), "Cart popup is empty, but it should contain at least one item.")

        # 6. Click "View cart" or similar button inside the popup.
        view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
        view_cart_button.click()

        # 7. On the cart page, verify that the product appears in the cart list.
        cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content")))
        self.assertTrue(cart_items.find_elements(By.CSS_SELECTOR, "tbody tr"), "The cart page does not contain any products, but it should.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()