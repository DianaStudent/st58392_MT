```python
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
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        home_page_html = html_data["home_page"]
        category_a_page_html = html_data["category_a_page"]
        product_page_html = html_data["product_page"]
        popup_html = html_data["popup"]

        # 1. Open home page. (Done in setUp)

        # 2. Click on product category.
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()
        except:
            self.fail("Category A link not found or not clickable.")

        # 3. Select the first product.
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except:
            self.fail("Product A link not found or not clickable.")

        # 4. Click the "Add to cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'is-success') and contains(@class, 'is-fullwidth')]"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable.")

        # 5. Click the cart icon/button to open the shopping bag.
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found or not clickable.")

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout' and contains(text(), 'Go to checkout')]"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed.")
        except:
            self.fail("GO TO CHECKOUT button not found.")

if __name__ == "__main__":
    html_data = {
  "home_page": "<body style=\"margin-top: 131px; zoom: 50%;\"> <div id=\"app\"><header><div class=\"container\"><div class=\"columns is-gapless is-mobile header-container\"><div class=\"column is-4 has-text-centered\"><a aria-current=\"page\" class=\"logo-image active\" href=\"/\"><img alt=\"logo\"/></a></div><div class=\"column is-4 has-text-right header-block-right\"><span class=\"icon icon-search is-hidden-tablet\"><img alt=\"Search\" src=\"/assets/images/search.svg\" style=\"min-width:24px\" title=\"Search\"/></span><span class=\"cart-button\"><img alt=\"cart\" class=\"icon\" src=\"/assets/images/shopping-bag.svg\" style=\"min-width:24px\" title=\"cart\"/></span><div><div class=\"mini-cart\"><p>Your cart is empty</p></div></div></div></div><div class=\"primary-nav is-hidden-mobile\"><ul class=\"nav-level-0\"><li class=\"has-items\"><div class=\"cat-parent\"><a class=\"has-items\" href=\"/category-a\">Category A</a></div><ul class=\"columns is-gapless is-multiline nav-level-1\"><li class=\"column is-3\"><div class=\"cat-parent\"><a href=\"/category-a-1\">Subcategory 1</a></div></li><li class=\"column is-3\"><div class=\"cat-parent\"><a href=\"/category-a-2\">Subcategory 2</a></div></li><li class=\"column is-3\"><div class=\"cat-parent\"><a href=\"/category-a-3\">Subcategory 3</a></div></li></ul></li><li><div class=\"cat-parent\"><a href=\"/category-b\">Category B</a></div></li><li><div class=\"cat-parent\"><a href=\"/category-c\">Category C</a></div></li></ul></div></div></header><div class=\"mobile-nav is-hidden-tablet\"><ul class=\"nav-level-0\"><li class=\"has-items\"><div class=\"cat-parent\"><a class=\"has-items\" href=\"/category-a\">Category A</a></div><ul class=\"columns is-gapless is-multiline nav-level-1\"><li class=\"column is-3\"><div class=\"cat-parent\"><a href=\"/category-a-1\">Subcategory 1</a></div></li><li class=\"column is-3\"><div class=\"cat-parent\"><a href=\"/category-a-2\">Subcategory 2</a></div></li><li class=\"column is-3\"><div class=\"cat-parent\"><a href=\"/category-a-3\">Subcategory 3</a></div></li></ul></li><li><div class=\"cat-parent\"><a href=\"/category-b\">Category B</a></div></li><li><div class=\"cat-parent\"><a href=\"/category-c\">Category C</a></div></li></ul></div><section class=\"section\" style=\"padding:0\"><div class=\"container\"><div class=\"home-slider\"><div aria-live=\"polite\" class=\"image-gallery\"><div class=\"image-gallery-content\"><div class=\"image-gallery-slide-wrapper bottom\"><div class=\"image-gallery-swipe\"><div class=\"image-gallery-slides\"><div class=\"image-gallery-slide center\" style=\"-webkit-transform:translate3d(0%, 0, 0);-moz-transform:translate3d(0%, 0, 0);-ms-transform:translate3d(0%, 0, 0);-o-transform:translate3d(0%, 0, 0);transform:translate3d(0%, 0, 0)\"><div class=\"image-gallery-image\"><a href=\"/page-1\"><img alt=\"THE FRESH FOAM CRUZ\" src=\"/assets/images/slide8.jpg\"/><div class=\"caption\" style=\"color:#ffffff\"><div class=\"caption-title\">THE FRESH FOAM CRUZ</div><div class=\"caption-description\">COMFORT. SPORT. STYLE.</div></div></a></div></div><div class=\"image-gallery-slide right\" style=\"-webkit-transform:translate3d(100%, 0, 0);-moz-transform:translate3d(100%, 0, 0);-ms-transform:translate3d(100%, 0, 0);-o-transform:translate3d(100%, 0, 0);transform:translate3d(100%, 0, 0)\"><div class=\"image-gallery-image\"><a href=\"/page-2\"><img src=\"/assets/images/slide9.jpg\"/></a></div></div><div class=\"image-gallery-slide left\" style=\"-webkit-transform:translate3d(-100%, 0, 0);-moz-transform:translate3d(-100%, 0, 0);-ms-transform:translate3d(-100%, 0, 0);-o-transform:translate3d(-100%, 0, 0);transform:translate3d(-100%, 0, 0)\"><div class=\"image-gallery-image\"><a href=\"/page-3\"><img src=\"/assets/