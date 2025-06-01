import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')  # Assuming this is the home page URL
    
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # 1. Open the home page.
        self.assertIn("localhost", driver.current_url)
        
        try:
            # 2. Click on the account icon/button in the top-right.
            account_icon = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button.account-setting-active")
            ))
            account_icon.click()

            # 3. Wait for the dropdown and click the "Login" link.
            login_link = wait.until(EC.presence_of_element_located(
                (By.LINK_TEXT, "Login")
            ))
            login_link.click()
            
            # 4. Wait for the login form to appear.
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-register-wrapper"))
            )
            
            # 5. Fill in the username and password fields using credentials.
            username_field = driver.find_element(By.NAME, "username")
            password_field = driver.find_element(By.NAME, "loginPassword")
        
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
            
            # 6. Click the login button.
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span")
            login_button.click()
            
            # 7. Wait for redirection or page update.
            wait.until(EC.url_contains("/my-account"))
            
            # 8. Confirm successful login by:
            # Verifying that the current URL contains "/my-account".
            self.assertIn("/my-account", driver.current_url)
        
        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()