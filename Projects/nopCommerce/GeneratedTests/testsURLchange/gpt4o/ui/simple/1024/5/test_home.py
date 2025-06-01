import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver

        try:
            # Check header elements
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))

            # Check links in the header
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

            # Check logo
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))

            # Check search box
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))

            # Check top menu
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))

            # Check footer
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))

        except Exception as e:
            self.fail(f"UI element missing or not visible: {str(e)}")

if __name__ == '__main__':
    unittest.main()