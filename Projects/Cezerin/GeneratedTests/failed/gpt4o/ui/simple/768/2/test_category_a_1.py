from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is missing or not visible")
        
        # Verify logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image.active")))
        except:
            self.fail("Logo is missing or not visible")

        # Verify search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box input.search-input")))
        except:
            self.fail("Search box is missing or not visible")
        
        # Verify cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img.icon")))
        except:
            self.fail("Cart button is missing or not visible")
        
        # Verify primary navigation
        try:
            primary_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav")))
        except:
            self.fail("Primary navigation is missing or not visible")

        # Verify category links
        category_links = ["Category A", "Category B", "Category C"]
        for category in category_links:
            try:
                category_link = wait.until(EC.visibility_of_element_located((
                    By.XPATH, f"//a[text()='{category}']"
                )))
            except:
                self.fail(f"Category link '{category}' is missing or not visible")

        # Verify breadcrumb navigation
        try:
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.breadcrumb")))
        except:
            self.fail("Breadcrumb navigation is missing or not visible")
        
        # Verify sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
        except:
            self.fail("Sort dropdown is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()