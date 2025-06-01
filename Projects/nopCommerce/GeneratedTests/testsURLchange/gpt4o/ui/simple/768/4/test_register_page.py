import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegisterPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/register?returnUrl=%2F")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_exist_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check headers
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))
        except:
            self.fail("Header elements are not visible.")

        # Check register button
        try:
            register_button = wait.until(EC.visibility_of_element_located(
                (By.ID, "register-button")))
        except:
            self.fail("Register button is not visible.")

        # Check form fields
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "gender-male")))
            wait.until(EC.visibility_of_element_located((By.ID, "gender-female")))
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Company")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        except:
            self.fail("Form fields are not visible.")

        # Check top menu links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        except:
            self.fail("Top menu links are not visible.")

if __name__ == "__main__":
    unittest.main()