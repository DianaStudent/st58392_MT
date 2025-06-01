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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://localhost/")
        
        # Accept cookies
        accept_cookies_btn = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
        if not accept_cookies_btn:
            self.fail("Cookie acceptance button not found.")
        accept_cookies_btn.click()

        # Step 2: Hover over a product image to reveal the "Add to cart" button
        product_img_selector = "//div[@class='product-img']/a[@href='/product/olive-table']/img"
        product_img = wait.until(EC.presence_of_element_located((By.XPATH, product_img_selector)))
        if not product_img:
            self.fail("Product image not found.")
        
        action = ActionChains(driver)
        action.move_to_element(product_img).perform()
        
        # Step 3: Click the "Add to cart" button
        add_to_cart_button_selector = "//button[@title='Add to cart']/i[@class='fa fa-shopping-cart']"
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_button_selector)))
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")
        add_to_cart_button.click()
        
        # Step 4: Open the cart popup by clicking the cart icon
        cart_icon_selector = "//button[@class='icon-cart']/i[@class='pe-7s-shopbag']"
        cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, cart_icon_selector)))
        if not cart_icon:
            self.fail("Cart icon not found.")
        cart_icon.click()
        
        # Step 5: Verify that at least one product is listed in the popup cart
        cart_popup_selector = "//div[@class='shopping-cart-content']/ul/li"
        cart_popup_items = wait.until(EC.presence_of_all_elements_located((By.XPATH, cart_popup_selector)))
        
        if not cart_popup_items or len(cart_popup_items) == 0:
            self.fail("No items found in the cart popup.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()