from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check visibility of header
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check visibility of footer
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Check visibility of navigation menu
            nav_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
            self.assertTrue(nav_menu.is_displayed(), "Navigation menu is not visible")

            # Check visibility of email input
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            # Check visibility of password input
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")

            # Check visibility of login button
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            # Check visibility of Register button
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")

            # Check visibility of search input
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Interact with elements
            register_button.click()
            WebDriverWait(driver, 20).until(EC.title_contains("Register"))
            driver.back()
            
            login_button.click()
            WebDriverWait(driver, 20).until(EC.title_contains("Login"))

        except Exception as e:
            self.fail(f"Test failed due to {str(e)}")

if __name__ == "__main__":
    unittest.main()