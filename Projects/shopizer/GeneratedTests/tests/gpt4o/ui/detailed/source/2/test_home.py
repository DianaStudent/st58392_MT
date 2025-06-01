import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//header[@class='header-area clearfix']")))
        self.assertTrue(header.is_displayed(), "Header is not displayed.")

        # Check footer is present and visible
        footer = wait.until(EC.visibility_of_element_located((By.XPATH, "//footer[@class='footer-area bg-gray']")))
        self.assertTrue(footer.is_displayed(), "Footer is not displayed.")
        
        # Check navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        self.assertTrue(home_link.is_displayed(), "Home link is not displayed.")
        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        self.assertTrue(tables_link.is_displayed(), "Tables link is not displayed.")
        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not displayed.")

        # Check call us text
        call_us_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Call Us : 888-888-8888')]")))
        self.assertTrue(call_us_text.is_displayed(), "Call us text is not displayed.")

        # Check for the main content
        main_content = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='site-blocks-cover']")))
        self.assertTrue(main_content.is_displayed(), "Main content area is not displayed.")

        # Check accept cookies button and click it
        accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not displayed.")
        accept_cookies_button.click()

        # Check subscriber email field
        email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        self.assertTrue(email_input.is_displayed(), "Email input field is not displayed.")

        # Check subscribe button and interact
        subscribe_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Subscribe')]")))
        self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not displayed.")
        subscribe_button.click()
        
    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()