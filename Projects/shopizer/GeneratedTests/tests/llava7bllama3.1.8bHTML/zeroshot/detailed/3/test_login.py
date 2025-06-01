from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page.
        self.driver.get("http://localhost:8080")

        # 2. Click on the account icon/button in the top-right.
        account_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.dropdown-toggle")))
        account_button.click()

        # 3. Wait for the dropdown and click the "Login" link.
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # 4. Wait for the login form to appear.
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))

        # 5. Fill in the username and password fields using credentials.
        email_field.send_keys("test2@user.com")
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("test**11")

        # 6. Click the login button.
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        login_button.click()

        # 7. Wait for redirection or page update.
        try:
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located((By.NAME, "email")))
        except TimeoutException:
            self.fail("Login form did not disappear")

        # 8. Confirm successful login by: Verifying that the current URL contains "/my-account".
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()