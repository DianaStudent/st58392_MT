import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPageUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence_and_visibility(self):
        try:
            # Check header element
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Check login link
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertIsNotNone(login_link)

            # Check registration link
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertIsNotNone(register_link)

            # Check main page links
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            self.assertIsNotNone(home_link)

            clothes_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            self.assertIsNotNone(clothes_link)

            accessories_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            self.assertIsNotNone(accessories_link)

            art_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            self.assertIsNotNone(art_link)

            # Check search field
            search_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertIsNotNone(search_field)

            # Check product listing
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertIsNotNone(product_list)

        except Exception as e:
            self.fail(f"UI element presence test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()