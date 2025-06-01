import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("data:text/html;charset=utf-8," + html_data["html"])

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is missing")

        # Check main navigation menu
        try:
            primary_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
        except:
            self.fail("Primary navigation menu is missing")
        
        # Check specific link in navigation
        try:
            category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
        except:
            self.fail("Category A link is missing")

        # Check subcategory link
        try:
            subcategory_1_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1')))
        except:
            self.fail("Subcategory 1 link is missing")

        # Check search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        except:
            self.fail("Search box is missing")

        # Check cart icon
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button')))
        except:
            self.fail("Cart button is missing")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()