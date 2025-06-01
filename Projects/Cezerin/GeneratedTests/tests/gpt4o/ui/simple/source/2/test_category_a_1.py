import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
    
        # Check header and logo
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img[alt='logo']")))
        except:
            self.fail("Header or logo not visible")

        # Check navigation links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 1")))
        except:
            self.fail("Navigation links not visible")

        # Check search input and cart
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input[placeholder='Search']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img[alt='cart']")))
        except:
            self.fail("Search input or cart icon not visible")

        # Check breadcrumb navigation
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
        except:
            self.fail("Breadcrumb navigation not visible")

        # Check sidebar filters and sorting
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar button")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort select")))
        except:
            self.fail("Sidebar filters or sorting not visible")

        # Check footer elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "About")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Privacy Policy")))
        except:
            self.fail("Footer elements not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()