import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check visibility of footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check visibility of navigation
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible.")

        # Check presence and visibility of input fields, buttons, labels, and sections
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible.")
        
        sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible.")
        
        contact_us_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        self.assertTrue(contact_us_link.is_displayed(), "Contact us link is not visible.")
        
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping-cart")
        self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible.")
        
        # Interact with key UI elements
        sign_in_button.click()
        
        # Confirm that UI reacts visually
        wait.until(EC.url_contains("http://localhost:8080/en/login"))
        current_url = driver.current_url
        self.assertIn("login", current_url, "Navigation to login page failed.")
        
        # Assert that no required UI element is missing
        try:
            driver.find_element(By.XPATH, "//h1[text()='Products']")
        except:
            self.fail("Required UI element 'Products' header is missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()