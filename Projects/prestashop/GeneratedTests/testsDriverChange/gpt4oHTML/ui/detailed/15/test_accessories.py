import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_interactions(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the presence and visibility of header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header:
            self.fail("Header is not visible.")

        # Check the presence and visibility of footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer:
            self.fail("Footer is not visible.")

        # Check the presence and visibility of the main navigation menu
        nav_menu = wait.until(EC.visibility_of_element_located((By.ID, "top-menu")))
        if not nav_menu:
            self.fail("Main navigation menu is not visible.")

        # Check the presence and visibility of input fields and buttons
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
        if not search_input:
            self.fail("Search input field is not visible.")

        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.material-icons.search")))
        if not search_button:
            self.fail("Search button is not visible.")

        sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        if not sign_in_link:
            self.fail("Sign in link is not visible.")

        # Interact with a key UI element, such as clicking the "Sign in" link
        sign_in_link.click()

        # Confirm that the UI reacts visually (e.g., navigates to the login page)
        current_url = driver.current_url
        expected_url = "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories"
        self.assertEqual(current_url, expected_url, "URL did not change to login page as expected.")

        # Assert the presence of important UI elements in login page
        login_form = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))
        if not login_form:
            self.fail("Login form is not visible after clicking sign in.")

if __name__ == "__main__":
    unittest.main()