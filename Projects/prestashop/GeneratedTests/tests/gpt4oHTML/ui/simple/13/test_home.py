import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or not visible")

        # Check main navigation links
        try:
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#category-3 a.dropdown-item')))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#category-6 a.dropdown-item')))
            art_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#category-9 a.dropdown-item')))
        except:
            self.fail("Main navigation links are missing or not visible")

        # Check Login
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in link is not present or not visible")

        # Check Register
        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
        except:
            self.fail("Create account link is not present or not visible")

        # Check Cart button
        try:
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.blockcart')))
        except:
            self.fail("Cart button is not present or not visible")

        # Check Search
        try:
            search_widget = self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except:
            self.fail("Search widget is not present or not visible")

        # Check footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not present or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()