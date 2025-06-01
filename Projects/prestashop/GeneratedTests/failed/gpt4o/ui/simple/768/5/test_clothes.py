from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header is not visible")
        
        # Check top menu elements
        try:
            top_menu_clothes = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            top_menu_accessories = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            top_menu_art = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("One or more top menu elements are not visible")

        # Check sign in link
        try:
            sign_in = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes']")))
        except:
            self.fail("Sign in link is not visible")

        # Check product listing
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, 'js-product-list')))
        except:
            self.fail("Product list is not visible")

        # Check filter section
        try:
            filter_section = wait.until(EC.visibility_of_element_located((By.ID, 'search_filters')))
        except:
            self.fail("Search filters are not visible")

        # Check newsletter subscription form
        try:
            newsletter = wait.until(EC.visibility_of_element_located((By.NAME, 'submitNewsletter')))
        except:
            self.fail("Newsletter subscription form is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()