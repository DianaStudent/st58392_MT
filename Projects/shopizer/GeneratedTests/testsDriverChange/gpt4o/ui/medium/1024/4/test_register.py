import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify the header logo is present and visible
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header .logo img')))
        self.assertTrue(logo.is_displayed(), "Logo is not visible")

        # Verify the navigation links are present
        nav_links = driver.find_elements(By.CSS_SELECTOR, 'header .main-menu nav ul li a')
        self.assertEqual(len(nav_links), 3, "Not all navigation links are present")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), "Navigation link is not visible")

        # Verify the presence of login and register tabs
        login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-rb-event-key, 'login')]")))
        register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-rb-event-key, 'register')]")))

        self.assertTrue(login_tab.is_displayed(), "Login tab is not visible")
        self.assertTrue(register_tab.is_displayed(), "Register tab is not visible")

        # Interact with the login tab
        login_tab.click()

        # Verify the presence of login form fields
        username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(span, 'Login')]")))

        self.assertTrue(username_input.is_displayed(), "Username input is not visible")
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")

        # Interact with an element and check UI update
        login_tab.click()  # Clicking login tab again to see visual feedback

        # Check no errors in UI after click
        self.assertTrue(driver.find_elements(By.CSS_SELECTOR, 'body'), "UI error after interaction")

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()