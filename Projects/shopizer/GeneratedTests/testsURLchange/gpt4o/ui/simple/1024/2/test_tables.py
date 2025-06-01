import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_ui_elements_visibility(self):
        driver = self.driver

        # Check for header links
        for link_text in ["Home", "Tables", "Chairs"]:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
            except:
                self.fail(f"Link '{link_text}' not found or not visible")

        # Check for account buttons
        try:
            account_btn = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_btn.click()

            for button_text in ["Login", "Register"]:
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, button_text))
                )
        except:
            self.fail("Account buttons are not visible or not found")

        # Check for cart button
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart"))
            )
        except:
            self.fail("Cart button is not visible or not found")

        # Check for subscribe form
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".button"))
            )
        except:
            self.fail("Subscribe form is not visible or not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()