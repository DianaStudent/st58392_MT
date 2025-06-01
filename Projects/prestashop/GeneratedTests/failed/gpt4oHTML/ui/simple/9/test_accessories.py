from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header
        try:
            header = self.wait.until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
        except:
            self.fail("Header is not visible")

        # Check for main menu links
        try:
            home_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']"))
            )
            clothes_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"))
            )
            accessories_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"))
            )
            art_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
        except:
            self.fail("One or more main menu links are not visible")

        # Check for login and register links
        try:
            login_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']"))
            )
            register_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']"))
            )
        except:
            self.fail("Login or Register link is not visible")

        # Check for products
        try:
            products = self.wait.until(
                EC.visibility_of_element_located((By.ID, "js-product-list"))
            )
        except:
            self.fail("Products list is not visible")

        # Check for filters
        try:
            filters = self.wait.until(
                EC.visibility_of_element_located((By.ID, "search_filters"))
            )
        except:
            self.fail("Filters are not visible")

        # Check for footer
        try:
            footer = self.wait.until(
                EC.visibility_of_element_located((By.ID, "footer"))
            )
        except:
            self.fail("Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()