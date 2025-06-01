import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")
    
    def test_key_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")
        
        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible.")
        
        # Check login link
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        except:
            self.fail("Login link is not visible.")

        # Check register link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Register link is not visible.")
        
        # Check search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input field is not visible.")
        
        # Check contact us link
        try:
            contact_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/contact-us']")))
        except:
            self.fail("Contact link is not visible.")

        # Check product list section
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "products")))
        except:
            self.fail("Product list section is not visible.")

        # Interact with search input field and submit
        try:
            search_input.send_keys("Art")
            search_input.submit()
        except:
            self.fail("Search functionality failed.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()