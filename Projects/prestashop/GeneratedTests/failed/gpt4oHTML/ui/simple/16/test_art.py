from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except Exception:
            self.fail("Header element not found or not visible.")
        
        # Check navigation links
        links_to_check = [
            ("home", "http://localhost:8080/en/"),
            ("clothes", "http://localhost:8080/en/3-clothes"),
            ("accessories", "http://localhost:8080/en/6-accessories"),
            ("art", "http://localhost:8080/en/9-art"),
            ("login", "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"),
            ("register", "http://localhost:8080/en/registration"),
        ]

        for _, link in links_to_check:
            try:
                nav_link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            except Exception:
                self.fail(f"Navigation link with href '{link}' not found or not visible.")

        # Check search form
        try:
            search_form = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except Exception:
            self.fail("Search form element not found or not visible.")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='s']")))
        except Exception:
            self.fail("Search input field not found or not visible.")

        # Check sign in button
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        except Exception:
            self.fail("Sign in button not found or not visible.")

        # Check cart
        try:
            cart = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
        except Exception:
            self.fail("Cart element not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()