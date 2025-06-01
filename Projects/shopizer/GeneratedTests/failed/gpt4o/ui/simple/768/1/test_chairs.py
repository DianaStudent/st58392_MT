from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header area and main menu
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
            logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo')))
            main_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-menu')))
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
        except:
            self.fail("Header area or main menu elements are missing or not visible")

        # Check login and register links
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Login or Register links are missing or not visible")

        # Check product elements
        try:
            product_list = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'product-wrap')))
            for product in product_list:
                self.assertTrue(product.is_displayed(), "A product is not visible")
        except:
            self.fail("Product elements are missing or not visible")

        # Check footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        except:
            self.fail("Footer area is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()