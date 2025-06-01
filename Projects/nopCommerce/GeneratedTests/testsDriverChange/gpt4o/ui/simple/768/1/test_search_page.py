import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-upper')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-lower')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-menu')))

            # Logo
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-logo')))

            # Search box
            wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
            wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))

            # Navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home page')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'New products')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Search')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My account')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Blog')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))

            # Product filter and results
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-filters')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'products-container')))

            # Product items
            products = driver.find_elements(By.CLASS_NAME, 'product-item')
            if not products:
                self.fail("No products found on the page.")

        except Exception as e:
            self.fail(f"UI element verification failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()