from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA1Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img[alt='logo']")))
            search_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.icon-search img[title='Search']")))
            cart_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-button img[alt='cart']")))
        except:
            self.fail("Header UI elements are missing or not visible.")

        # Check navigation links
        try:
            nav_links = [
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A"))),
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B"))),
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C"))),
            ]
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check breadcrumb
        try:
            breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.breadcrumb")))
            home_breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.breadcrumb a.active[aria-current='page']")))
        except:
            self.fail("Breadcrumb navigation is missing or not visible.")

        # Check Sort dropdown
        try:
            sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.select select")))
        except:
            self.fail("Sort dropdown is missing or not visible.")
        
        # Interact: Toggle sort dropdown
        try:
            sort_dropdown.click()
            favorite_option = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='stock_status,price,position']")))
            favorite_option.click()
        except:
            self.fail("Could not interact with the sort dropdown.")
        
        # Check footer sections
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            footer_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-logo img[alt='logo']")))
        except:
            self.fail("Footer UI elements are missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()