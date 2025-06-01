import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothingPageUI(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements_presence(self):
        driver = self.driver

        try:
            # Wait for and check if the header is visible
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
            
            # Check if the main title "Clothes" is present
            main_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1"))
            )

            # Check if the product list is visible
            product_list = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "js-product-list"))
            )

            # Check if the top menu (nav) is visible
            top_menu = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "_desktop_top_menu"))
            )

            # Check if the login link is visible
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )

            # Check if the newsletter field is visible
            newsletter = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )

            # Check if the shopping cart is visible
            cart = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))
            )
            
        except Exception as e:
            self.fail(f"An expected UI element is missing: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()