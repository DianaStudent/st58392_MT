import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UIElementsTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header")))
            
            # Check login and register links
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-login")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-register")))
            
            # Check search box
            wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            
            # Check header menu items
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))

            # Check footer elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))

        except Exception as e:
            self.fail(f"UI elements check failed: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()