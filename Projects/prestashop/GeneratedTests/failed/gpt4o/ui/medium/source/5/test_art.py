from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of header elements
        try:
            element = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or visible")

        # Check presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("One or more navigation links are not present or visible")

        # Check presence of login and register buttons
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Login or Register button is not present or visible")

        # Check presence of product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is not present or visible")

        # Interact with an element, e.g., click on a product link
        try:
            product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='the-best-is-yet-to-come-framed-poster']")))
            product_link.click()
            # Check that the product page opens by confirming the presence of the product image or title
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src*='the-best-is-yet-to-come-framed-poster']")))
        except:
            self.fail("Product interaction failed or the product page did not load as expected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()