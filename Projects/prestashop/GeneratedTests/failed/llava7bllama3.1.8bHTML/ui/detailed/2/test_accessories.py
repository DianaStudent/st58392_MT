from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopifyPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_shop_page_structure(self):
        # Wait for elements to be visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check visibility of main UI components
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())

    def test_clothes_page_structure(self):
        self.driver.get("http://localhost:8080/en/3-clothes")

        # Wait for elements to be visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check visibility of main UI components
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())

    def test_login_page_structure(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Wait for elements to be visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check visibility of main UI components
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())

    def test_register_page_structure(self):
        self.driver.get("http://localhost:8080/en/registration")

        # Wait for elements to be visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check visibility of main UI components
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())

    def test_login_button_click(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Wait for login button to be clickable
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitLogin")))

        # Click on the button
        login_button.click()

    def test_required_elements(self):
        required_elements = ["header", "footer", "nav"]

        for element in required_elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"#{element}")))
            except TimeoutException:
                self.fail(f"Element {element} is missing")

if __name__ == "__main__":
    unittest.main()