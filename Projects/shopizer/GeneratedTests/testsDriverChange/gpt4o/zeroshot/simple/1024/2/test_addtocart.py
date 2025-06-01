import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        try:
            # Add product to cart
            product_selector = (By.CSS_SELECTOR, "div.product-wrap-2")
            add_to_cart_button_selector = (By.CSS_SELECTOR, "button[title='Add to cart']")

            product_element = wait.until(EC.presence_of_element_located(product_selector))
            ActionChains(driver).move_to_element(product_element).perform()

            add_to_cart_button = product_element.find_element(*add_to_cart_button_selector)
            add_to_cart_button.click()

            # Open cart popup
            cart_icon_selector = (By.CSS_SELECTOR, "button.icon-cart")
            cart_icon = wait.until(EC.element_to_be_clickable(cart_icon_selector))
            cart_icon.click()

            # Confirm success by checking that the popup contains at least one item
            item_in_cart_selector = (By.CSS_SELECTOR, "ul > li.single-shopping-cart")
            items_in_cart = wait.until(EC.presence_of_all_elements_located(item_in_cart_selector))
            
            self.assertGreater(len(items_in_cart), 0, "No items found in the cart popup")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


if __name__ == "__main__":
    unittest.main()