from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements_presence(self):
        driver = self.driver

        try:
            # Wait for and check header visibility
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check the visibility of the main navigation links
            clothes_link = header.find_element(By.LINK_TEXT, "Clothes")
            accessories_link = header.find_element(By.LINK_TEXT, "Accessories")
            art_link = header.find_element(By.LINK_TEXT, "Art")
            
            # Check the login link
            login_link = header.find_element(By.LINK_TEXT, "Sign in")
            
            # Wait for and check footer visibility
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Check if search field is visible
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Check if subscription field is visible
            newsletter_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))

            # Check the 'Subscribe' button
            subscribe_button = newsletter_input.find_element(By.XPATH, "../..//input[@value='Subscribe']")
            
            # Click on 'Sign in' link to ensure interaction works
            login_link.click()
            self.wait.until(EC.url_contains("login"))

        except Exception as e:
            self.fail(f"A required UI element is missing or not interactable: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()