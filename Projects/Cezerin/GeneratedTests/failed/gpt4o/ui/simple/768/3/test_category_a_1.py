from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-search')))
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
            nav_bar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
        except:
            self.fail("Header elements are not present or visible.")

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            category_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            subcategory_1_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']")))
        except:
            self.fail("Navigation links are not present or visible.")

        # Check category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        except:
            self.fail("Category title is not present or visible.")

        # Check footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            footer_contact_1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='footer-contacts']/li[text()='104 N Stagecoach Rd']")))
            footer_service_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about']")))
        except:
            self.fail("Footer elements are not present or visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()