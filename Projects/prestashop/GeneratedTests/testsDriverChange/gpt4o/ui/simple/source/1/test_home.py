import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header#header")))
        except:
            self.fail("Header is not visible")

        # Check menu items
        menu_items = [
            "a[href='http://localhost:8080/en/3-clothes']",
            "a[href='http://localhost:8080/en/6-accessories']",
            "a[href='http://localhost:8080/en/9-art']"
        ]
        for item in menu_items:
            try:
                element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, item)))
                self.assertTrue(element.is_displayed())
            except:
                self.fail(f"Menu item {item} is not visible")

        # Check sign in link
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")))
            self.assertTrue(sign_in_link.is_displayed())
        except:
            self.fail("Sign in link is not visible")

        # Check register link
        try:
            register_link = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
            self.assertTrue(register_link.is_displayed())
        except:
            self.fail("Register link is not visible")
        
        # Check search bar
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            self.assertTrue(search_bar.is_displayed())
        except:
            self.fail("Search bar is not visible")

        # Check shopping cart
        try:
            cart = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "div.blockcart.cart-preview")))
            self.assertTrue(cart.is_displayed())
        except:
            self.fail("Shopping cart is not visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer#footer")))
            self.assertTrue(footer.is_displayed())
        except:
            self.fail("Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()