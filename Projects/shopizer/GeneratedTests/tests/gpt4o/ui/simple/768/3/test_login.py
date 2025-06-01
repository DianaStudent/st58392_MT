import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        try:
            # Check header logo
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo a img')))
            
            # Check navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))

            # Check login and register tabs
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.nav-link.active')))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[role="tab"][data-rb-event-key="register"]')))

            # Check login form fields
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))

            # Check remember me checkbox
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-toggle-btn input[type="checkbox"]')))

            # Check login button
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-box button')))
            
            # Check footer elements
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()