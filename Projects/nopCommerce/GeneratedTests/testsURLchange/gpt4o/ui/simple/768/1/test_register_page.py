import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegisterPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_page_ui_elements(self):
        # Verify header links
        self._assert_element_present(By.LINK_TEXT, "Register")
        self._assert_element_present(By.LINK_TEXT, "Log in")
        self._assert_element_present(By.LINK_TEXT, "Wishlist")
        self._assert_element_present(By.LINK_TEXT, "Shopping cart")

        # Verify search box
        self._assert_element_present(By.ID, "small-searchterms")
        self._assert_element_present(By.CLASS_NAME, "search-box-button")
    
        # Verify registration form fields
        self._assert_element_present(By.ID, "gender-male")
        self._assert_element_present(By.ID, "gender-female")
        self._assert_element_present(By.ID, "FirstName")
        self._assert_element_present(By.ID, "LastName")
        self._assert_element_present(By.ID, "Email")
        self._assert_element_present(By.ID, "Company")
        self._assert_element_present(By.ID, "Newsletter")
        self._assert_element_present(By.ID, "Password")
        self._assert_element_present(By.ID, "ConfirmPassword")
        
        # Verify submit button
        self._assert_element_present(By.ID, "register-button")

    def _assert_element_present(self, by, identifier):
        try:
            self.wait.until(EC.visibility_of_element_located((by, identifier)))
        except:
            self.fail(f"Element not present or visible: {identifier}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()