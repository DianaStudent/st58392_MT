import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("about:blank")
        self.driver.execute_script("document.write(arguments[0])", html_data["html"])
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components_exist(self):
        driver = self.driver
        wait = self.wait
        
        # Check Header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header:
            self.fail("Header is missing")
        
        # Check Navbar (elements in header)
        logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        if not logo:
            self.fail("Logo link is missing")
        
        # Check main Navigation links
        nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav .nav-level-0 > li > .cat-parent > a')))
        if not nav_links or len(nav_links) < 3:
            self.fail("Main navigation links are missing")

        # Check Subcategories links in mobile navbar
        mobile_nav_subcategories = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.mobile-nav .nav-level-1 .cat-parent > a')))
        if not mobile_nav_subcategories or len(mobile_nav_subcategories) < 3:
            self.fail("Mobile navbar subcategories are missing")
        
        # Check Search input and icon
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        if not search_input:
            self.fail("Search input is missing")
        search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        if not search_icon:
            self.fail("Search icon is missing")
        
        # Check Cart button/icon
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        if not cart_button:
            self.fail("Cart button/icon is missing")
        
        # Check Footer links
        footer_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'footer .footer-menu a')))
        if not footer_links:
            self.fail("Footer links are missing")
        
        # Check Breadcrumbs
        breadcrumbs = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
        if not breadcrumbs:
            self.fail("Breadcrumbs are missing")
        
        # Check Category Title
        category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        if not category_title:
            self.fail("Category title is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()