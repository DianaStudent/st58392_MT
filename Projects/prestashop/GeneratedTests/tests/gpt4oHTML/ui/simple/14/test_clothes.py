import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"

    def test_ui_components(self):
        driver = self.driver
        driver.get(self.base_url)
        
        try:
            # Check for header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
        except:
            self.fail("Header not found or not visible.")
        
        try:
            # Check for top menu links
            clothes_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
        except:
            self.fail("Clothes link not found or not visible.")
        
        try:
            accessories_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
            )
        except:
            self.fail("Accessories link not found or not visible.")
        
        try:
            # Check for login link
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='login']"))
            )
        except:
            self.fail("Login link not found or not visible.")
        
        try:
            # Check for register link
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='registration']"))
            )
        except:
            self.fail("Register link not found or not visible.")

        try:
            # Check for search input field
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']"))
            )
        except:
            self.fail("Search input field not found or not visible.")
        
        try:
            # Check for cart in header
            cart_icon = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart"))
            )
        except:
            self.fail("Cart icon not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()