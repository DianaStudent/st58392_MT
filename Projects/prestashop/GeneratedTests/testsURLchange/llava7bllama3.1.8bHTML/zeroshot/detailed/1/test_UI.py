import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebshop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        # Wait for the header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        
        # Check presence and visibility of main UI components
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "#logo").is_displayed())
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".navigation-menu").is_displayed())
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".searchbar input").is_displayed())
        
        # Interact with key UI elements
        self.driver.find_element(By.CSS_SELECTOR, "#logo").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".category-menu")))
        self.driver.find_element(By.CSS_SELECTOR, "[data-category='clothes']").click()
        
    def test_login_page(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        
        # Check presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".login-form input[name='email']").is_displayed())
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".login-form button[type='submit']").is_displayed())
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "#register-link").is_displayed())

if __name__ == "__main__":
    unittest.main()