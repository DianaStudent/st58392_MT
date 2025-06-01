import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver
        
        # Wait for elements to be present
        try:
            # Check logo
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "img.logo"))
            )
            
            # Check for contact us link
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#contact-link a[href='/en/contact-us']"))
            )

            # Check for the Sign in link
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']"))
            )

            # Check for the Cart link
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".blockcart"))
            )

            # Check for top menu (Clothes, Accessories, Art)
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/3-clothes']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/6-accessories']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/9-art']"))
            )

            # Check for login form fields
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            # Check for 'No account? Create one here' link
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/registration']"))
            )

            # Check for 'Forgot your password?' link
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/password-recovery']"))
            )

            # Check for 'Sign in' button
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "submit-login"))
            )
        
        except Exception as e:
            self.fail(f"Failed to find a UI element: {str(e)}")
        
if __name__ == "__main__":
    unittest.main()