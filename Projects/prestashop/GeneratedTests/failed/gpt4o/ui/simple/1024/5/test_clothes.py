from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements_present_and_visible(self):
        # Verify header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or not visible.")

        # Verify navigation links
        try:
            nav_links = [
                "http://localhost:8080/en/3-clothes",
                "http://localhost:8080/en/6-accessories",
                "http://localhost:8080/en/9-art",
            ]
            for link in nav_links:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
        except:
            self.fail("Navigation links are not all present or not visible.")

        # Verify sign-in button
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        except:
            self.fail("Sign-in button is not present or not visible.")

        # Verify search bar
        try:
            search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))
        except:
            self.fail("Search bar is not present or not visible.")

        # Verify product section
        try:
            product_section = self.wait.until(EC.visibility_of_element_located((By.ID, "products")))
        except:
            self.fail("Product section is not present or not visible.")

        # Verify filter buttons (e.g., Filter By)
        try:
            filter_by = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='text-uppercase h6 hidden-sm-down' and text()='Filter By']")))
        except:
            self.fail("Filter By section is not present or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()