from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class MainPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def test_main_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))
            
            # Logo
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
            
            # Search box
            wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            
            # Navigation menu
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile")))
            
            # Main content
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "master-wrapper-content")))

            # Footer elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-upper")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-lower")))

            # Buttons and links
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-register")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-login")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-wishlist")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-cart")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))

        except Exception as e:
            self.fail(f"Failed to find an element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()