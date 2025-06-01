import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/login?returnUrl=%2F")
        self.driver.maximize_window()

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of navigation menu links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        except Exception:
            self.fail("One or more navigation links are missing or not visible.")

        # Check presence of form fields
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))
        except Exception:
            self.fail("One or more form fields are missing or not visible.")

        # Check presence of buttons
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
        except Exception:
            self.fail("Register or login button is missing or not visible.")

        # Check interaction with the login button, should not cause error in UI
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
            login_button.click()
        except Exception:
            self.fail("Clicking the login button caused an error.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()