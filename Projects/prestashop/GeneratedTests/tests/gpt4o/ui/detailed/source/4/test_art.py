import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check footer visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible")
        
        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("One or more navigation links are not visible")

        # Check login and register links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Login or Register links are not visible")

        # Check product list and related elements
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            
            # Verify the first product and its quick view button
            first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-product")))
            quick_view_button = first_product.find_element(By.CSS_SELECTOR, ".quick-view.js-quick-view")
            quick_view_button.click()
            
            # Confirm quick view action
            modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        except:
            self.fail("Unable to display product quick view")
        
        # Ensure search widget is present
        try:
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except:
            self.fail("Search widget is not visible")

        # Ensure product filter is present
        try:
            search_filters = wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))
        except:
            self.fail("Search filters are not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()