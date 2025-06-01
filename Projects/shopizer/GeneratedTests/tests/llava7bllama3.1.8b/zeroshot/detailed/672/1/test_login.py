import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def test_login(self):
        # 1. Click on the account icon/button in the top-right.
        account_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='account']"))
        )
        account_icon.click()

        # 2. Wait for the dropdown and click the "Login" link.
        login_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # 3. Fill in the username and password fields using credentials.
        username_field = self.driver.find_element_by_name("email")
        username_field.send_keys("test2@user.com")

        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys("test**11")

        # 4. Click the login button.
        login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        # 5. Wait for redirection or page update.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )

        # 6. Confirm successful login by verifying that the current URL contains "/my-account".
        self.assertIn("/my-account", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()