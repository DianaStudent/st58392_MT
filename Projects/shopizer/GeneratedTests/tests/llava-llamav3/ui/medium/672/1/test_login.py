import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriver
from selenium.webdriver.support.select import Select

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        driver = ChromeDriver()
        self.driver = driver
        self.assertTrue(self.driver.title().lower() == "shopper")
        
    def tearDown(self):
        self.driver.quit()

    def test_login_page_loads_successfully(self):
        self.driver.get("http://localhost/login")
        self.assertTrue("Login" in self.driver.title())
        self.assertEqual(self.driver.current_url, "http://localhost/login")
        self.driver.find_element(by=By.ID, id="email").send_keys("test@email.com")
        self.driver.find_element(by=By.ID, id="password").send_keys("testpassword123")
        self.driver.find_element(by=By.ID, id="remember").click()
        self.assertTrue(self.driver.current_url, "http://localhost/dashboard")
    
if __name__ == "__main__":
    unittest.main(tests=[TestLoginPage])