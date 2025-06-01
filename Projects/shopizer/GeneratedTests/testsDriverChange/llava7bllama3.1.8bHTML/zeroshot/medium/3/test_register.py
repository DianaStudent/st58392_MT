import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        
    def test_register(self):
        # Step 1: Click on the account button and select "Register"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))).click()
        
        # Step 2: Fill in the registration form
        email = self.driver.find_element(By.NAME, 'email')
        password = self.driver.find_element(By.NAME, 'password')
        first_name = self.driver.find_element(By.NAME, 'first_name')
        last_name = self.driver.find_element(By.NAME, 'last_name')
        
        # Dynamically generate email
        import random
from selenium.webdriver.chrome.service import Service as ChromeService
        email.send_keys(f'test{random.randint(1000, 9999)}@test.com')
        password.send_keys('test**11')
        first_name.send_keys('Test')
        last_name.send_keys('User')
        
        # Step 3: Select a country and a region/state
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'country'))).send_keys('USA')
        self.driver.find_element(By.XPATH, "//select[@name='region']").find_element_by_xpath("//option[.='California']").click()
        
        # Step 4: Submit the registration form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'submit'))).click()
        
        # Step 5: Wait for redirect and confirm success by checking if the current URL includes "/my-account"
        self.assertEqual(self.driver.current_url, '/my-account')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()