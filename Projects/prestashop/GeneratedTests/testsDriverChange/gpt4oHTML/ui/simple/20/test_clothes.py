from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check the presence of the header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except Exception as e:
            self.fail("Header not found: " + str(e))

        # Check the presence of 'Sign in' link
        try:
            sign_in = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes']"
            )))
        except Exception as e:
            self.fail("Sign in link not found: " + str(e))

        # Check the presence of the cart element
        try:
            cart = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
        except Exception as e:
            self.fail("Cart element not found: " + str(e))

        # Check the presence of the main category links
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"
            )))
        except Exception as e:
            self.fail("Clothes link not found: " + str(e))
        
        try:
            accessories_link = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"
            )))
        except Exception as e:
            self.fail("Accessories link not found: " + str(e))

        try:
            art_link = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"
            )))
        except Exception as e:
            self.fail("Art link not found: " + str(e))

        # Check the presence of the search widget
        try:
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except Exception as e:
            self.fail("Search widget not found: " + str(e))

        # Check for product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except Exception as e:
            self.fail("Product list not found: " + str(e))

        # Check newsletter subscription field in footer
        try:
            newsletter = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//input[@placeholder='Your email address']"
            )))
        except Exception as e:
            self.fail("Newsletter subscription field not found: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)