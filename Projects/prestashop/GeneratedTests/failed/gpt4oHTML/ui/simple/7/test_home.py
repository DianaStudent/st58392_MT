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

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or visible")

        # Check links
        try:
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
            self.fail("One or more category links are not present or visible")

        # Check login and register links
        try:
            login_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']"))
            )
            register_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']"))
            )
        except:
            self.fail("Login or register link is not present or visible")

        # Check if the search bar is present
        try:
            search_bar = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='s']"))
            )
        except:
            self.fail("Search bar is not present or visible")

        # Check if the cart and sign in buttons are present
        try:
            cart_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='_desktop_cart']"))
            )
            sign_in_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']"))
            )
        except:
            self.fail("Cart or sign in button is not present or visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()