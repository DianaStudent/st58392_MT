from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from unittest import TestCase
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

class TestRegisterPage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.register_page = "http://localhost:8080/registration"
        self.login_page = "http://localhost:8080/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"
    
    def tearDown(self):
        self.driver.quit()

    def test_register_page(self):
        self.driver.get(self.register_page)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()