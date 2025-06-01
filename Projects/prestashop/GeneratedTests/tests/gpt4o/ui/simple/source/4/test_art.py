import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check main navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible")

            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.assertTrue(accessories_link.is_displayed(), "Accessories link is not visible")

            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            self.assertTrue(art_link.is_displayed(), "Art link is not visible")

            # Check login and register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(login_link.is_displayed(), "Sign in link is not visible")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
            self.assertTrue(register_link.is_displayed(), "Create account link is not visible")

            # Check that the search form field is present
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check product list
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertTrue(product_list.is_displayed(), "Product list is not visible")

            # Check footer
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

        except Exception as e:
            self.fail(f"UI element test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()