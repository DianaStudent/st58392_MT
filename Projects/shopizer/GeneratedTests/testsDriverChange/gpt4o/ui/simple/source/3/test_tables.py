import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header elements
            header_logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/' and contains(@class, 'logo')]")))
            self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")

            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

            # Check login and register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")

            # Check cart icon
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible")

            # Check product elements
            product_image = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='default-img']")))
            self.assertTrue(product_image.is_displayed(), "Product image is not visible")

            add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
            self.assertTrue(add_to_cart_button.is_displayed(), "Add to cart button is not visible")

            # Check footer elements
            footer_logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'footer-logo')]//a[@href='/']")))
            self.assertTrue(footer_logo.is_displayed(), "Footer logo is not visible")
            
        except Exception as e:
            self.fail(f"UI element validation failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()