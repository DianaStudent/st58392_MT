import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Header links are missing")

        # Check login and register links
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Login/Register links are missing")

        # Check cart button
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        except:
            self.fail("Cart button is missing")

        # Check main banner existence
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".site-blocks-cover img")))
        except:
            self.fail("Main banner image is missing")

        # Check product tab and products
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-tab-list")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        except:
            self.fail("Product tab or products are missing")

        # Check subscribe form
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form input[name='email']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .button")))
        except:
            self.fail("Subscribe form is missing")

        # Check footer links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Footer links are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()