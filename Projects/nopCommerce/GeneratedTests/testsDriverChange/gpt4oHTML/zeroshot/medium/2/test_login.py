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
        self.driver.maximize_window()
        self.driver.get("http://max/")  # Replace with actual URL
    
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify Home Page is loaded
        try:
            home_page_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Home page']")))
            self.assertTrue(home_page_link.is_displayed())
        except:
            self.fail("Home page not loaded or 'Home page' link not found")

        # Click on "My account" to go to the login page
        try:
            my_account_link = driver.find_element(By.XPATH, "//a[text()='My account']")
            self.assertTrue(my_account_link.is_displayed())
            my_account_link.click()
        except:
            self.fail("My account link not found on home page")

        # Wait for and verify Login Page
        try:
            login_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Welcome, Please Sign In!']")))
            self.assertTrue(login_title.is_displayed())
        except:
            self.fail("Login Page not loaded or login title not present")
        
        # Enter email and password
        try:
            email_input = driver.find_element(By.ID, "Email")
            password_input = driver.find_element(By.ID, "Password")
            self.assertTrue(email_input.is_displayed() and password_input.is_displayed())
            
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except:
            self.fail("Email or Password input fields missing")
        
        # Click on "Log in" button
        try:
            login_button = driver.find_element(By.XPATH, "//button[@class='button-1 login-button']")
            self.assertTrue(login_button.is_displayed())
            login_button.click()
        except:
            self.fail("Login button not found or not clickable")
        
        # Verify login success by "Log out" button
        try:
            logout_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Log out']")))
            self.assertTrue(logout_link.is_displayed())
        except:
            self.fail("Log out link not found, login might have failed")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()