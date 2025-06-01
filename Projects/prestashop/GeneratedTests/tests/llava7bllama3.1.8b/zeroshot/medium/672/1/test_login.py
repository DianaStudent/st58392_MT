import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        # Click on the login link in the top menu
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))

        # Fill in the email and password fields
        self.driver.find_element(By.ID, "email").send_keys("test@user.com")
        self.driver.find_element(By.ID, "password").send_keys("test@user1")

        # Submit the login form
        self.driver.find_element(By.ID, "login-button").click()

        # Verify that login was successful by checking for the presence of "Sign out" in the top bar
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()