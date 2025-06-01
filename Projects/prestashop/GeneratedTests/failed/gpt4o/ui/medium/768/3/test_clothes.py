from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not present or visible.")

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

        except:
            self.fail("One or more navigation links are not present or visible.")
        
        # Check input field (Search)
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
        except:
            self.fail("Search input not present or visible.")

        # Check button (Search icon)
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.material-icons.search")))
        except:
            self.fail("Search button not present or visible.")
        
        # Check and interact with 'Sign in' link
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()

            # Verify redirect to login page
            wait.until(EC.url_contains("login"))
        
        except:
            self.fail("Sign in link is not functioning correctly.")
        
        # Verify no errors on sign-in click
        self.assertNotIn("error", driver.page_source.lower(), "UI contains errors after sign-in interaction.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()