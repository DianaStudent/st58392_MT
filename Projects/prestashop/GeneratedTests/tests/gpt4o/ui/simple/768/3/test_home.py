from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed())
        except Exception:
            self.fail("Header not visible")

        # Check for search input in search widget
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[name='s']")))
            self.assertTrue(search_input.is_displayed())
        except Exception:
            self.fail("Search input not visible")

        # Check for login link
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(login_link.is_displayed() and login_link.get_attribute("href") == "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F")
        except Exception:
            self.fail("Login link not visible")

        # Check for register link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
            self.assertTrue(register_link.is_displayed() and register_link.get_attribute("href") == "http://localhost:8080/en/registration")
        except Exception:
            self.fail("Register link not visible")

        # Check for nav links
        category_links = [
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
        ]
        
        for text, href in category_links:
            try:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
                self.assertTrue(link.is_displayed() and link.get_attribute("href") == href)
            except Exception:
                self.fail(f"{text} link not visible")

        # Check for cart link
        try:
            cart_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_cart .cart-products-count")))
            self.assertTrue(cart_link.is_displayed())
        except Exception:
            self.fail("Cart link not visible")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()