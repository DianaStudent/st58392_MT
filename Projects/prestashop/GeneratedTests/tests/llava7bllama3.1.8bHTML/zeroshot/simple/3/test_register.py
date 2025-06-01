import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080") # URL for the webpage to test
    
    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-name='email']")))
        password_input = self.driver.find_element(By.XPATH, "//input[@data-name='password']")
        
        if not email_input or not password_input:
            self.fail("Email and/or Password input field(s) are missing.")
            
        # Fill in the registration form
        email_input.send_keys("test@user1")
        password_input.send_keys("test@user1")

        # Find the register button and click it
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='register']"))).click()
        
        # Wait for a sign out link to appear
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-name='sign-out']"))))
        
if __name__ == "__main__":
    unittest.main(argv=[], verbosity=2)