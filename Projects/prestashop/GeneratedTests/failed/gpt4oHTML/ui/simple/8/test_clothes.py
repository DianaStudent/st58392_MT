from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check for navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check for logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src,'logo.png')]")))
        except:
            self.fail("Logo is missing or not visible.")

        # Check for search bar
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][name='s']")))
        except:
            self.fail("Search bar is missing or not visible.")

        # Check for products
        try:
            product_list = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-miniature")))
            if not product_list:
                self.fail("Product list is empty or not visible.")
        except:
            self.fail("Product list is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()