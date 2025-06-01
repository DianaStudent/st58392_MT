import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header not found or not visible.")

        # Check main menu items
        for menu_item in ["Home", "Tables", "Chairs"]:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, menu_item)))
            except:
                self.fail(f"{menu_item} link not found or not visible.")

        # Check login and register links
        for link_text in ["Login", "Register"]:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"{link_text} link not found or not visible.")

        # Check product add to cart buttons
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[title='Add to cart']")))
        except:
            self.fail("Add to cart button not found or not visible.")

        # Check footer elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()