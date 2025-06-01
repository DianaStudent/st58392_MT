import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not visible on the page")

        # Check footer visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is not visible on the page")

        # Check search box presence and interaction
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            
            search_box.send_keys("Test")
            search_button.click()
            
            # Wait for search results - checking URL change as a proxy
            wait.until(EC.url_contains('/search?q=Test'))
        except:
            self.fail("Search box or button is not functional")

        # Check registration and login link visibility
        try:
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            login_link = driver.find_element(By.LINK_TEXT, "Log in")
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")
        except:
            self.fail("Register or login link is not visible or clickable")

        # Check newsletter subscription functionality
        try:
            newsletter_email = driver.find_element(By.ID, "newsletter-email")
            newsletter_button = driver.find_element(By.ID, "newsletter-subscribe-button")
            
            newsletter_email.send_keys("test@example.com")
            newsletter_button.click()
            
            # Wait for result message to appear - proxy for checking response
            result_message = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-result-block")))
            self.assertTrue(result_message.is_displayed(), "Newsletter subscription result is not visible")
        except:
            self.fail("Newsletter subscription is not functional")

        # Check navigation menu
        try:
            top_menu = driver.find_element(By.CLASS_NAME, "top-menu")
            self.assertTrue(top_menu.is_displayed(), "Top menu is not visible")
        except:
            self.fail("Top menu is not visible or clickable")

    def tearDown(self):
        # Quit the browser session
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()