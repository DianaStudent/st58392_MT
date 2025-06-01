import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check header
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            self.assertTrue(header.is_displayed())

            # Check navigation links
            nav_links = ["Home", "Tables", "Chairs"]
            for link_text in nav_links:
                nav_link = self.wait.until(EC.visibility_of_element_located(
                    (By.LINK_TEXT, link_text)))
                self.assertTrue(nav_link.is_displayed())

            # Check login and register links in account dropdown
            account_button = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "account-setting-active")))
            account_button.click()

            login_link = self.wait.until(EC.visibility_of_element_located(
                (By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed())

            register_link = self.wait.until(EC.visibility_of_element_located(
                (By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed())

            # Check product list visibility
            product_list = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "product-wrap")))
            self.assertTrue(product_list.is_displayed())

            # Check presence of add to cart button for a product
            add_to_cart_buttons = self.wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "button[title='Add to cart']")))
            self.assertTrue(all(button.is_displayed() for button in add_to_cart_buttons))

            # Click on the 'Accept' cookies button if it exists
            try:
                accept_cookies_button = self.wait.until(EC.visibility_of_element_located(
                    (By.ID, "rcc-confirm-button")))
                accept_cookies_button.click()
            except:
                pass

            # Check footer
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
            self.assertTrue(footer.is_displayed())

        except Exception as e:
            self.fail(f"A required UI element is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()