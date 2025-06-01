import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.actions import KeyAction
from selenium.webdriver.common.keys import Key

class TestLogin(unittest.TestCase):
```css
    def setUp(self):
        # Set up a new Chrome browser session.
        self.driver = webdriver.Chrome(options=Options())
        self.email_field = (By.XPATH, "//input[@name='email']")
        self.password_field = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[contains(text(), 'Login')]")

    def tearDown(self):
        # Close the browser session.
        self.driver.quit()
```

```scss
    def test_login(self):
        self.driver.get("http://localhost/")
        account_icon = self.wait_for_element_located((By.XPATH, "//img[@alt='Account icon']"))
        login_link = self.wait_for_element_located((By.XPATH, "//a[contains(text(), 'Login')]"))
        account_icon.click()
        login_link.click()

        email_field = self.wait_for_element_located(self.email_field)
        password_field = self.wait_for_element_located(self.password_field)

        email_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        self.login_button = self.wait_for_element_located(self.login_button)
        self.login_button.click()

        self.assertTrue("/my-account" in self.driver.current_url, "Login failed")
```
In the code above, we use WebDriver to manage a new Chrome browser session. We define several elements based on their relative positions and content, such as the account icon button, login link button, email field, password field, and login button.

We then perform the following steps:
1. Open the home page
2. Click on the account icon/button in the top-right corner
3. Wait for the dropdown and click the "Login" link
4. Wait for the login form to appear
5. Fill in the username and password fields using credentials
6. Click the login button
7. Wait for redirection or page update
8. Confirm successful login by verifying that the current URL contains "/my-account"

We use the `assert` function to confirm if the login was successful, and fail the test if it wasn't. We also set up a `setUp()` method to create a new Chrome browser session before running each test case, and a `tearDown()` method to close the browser session after each test case.