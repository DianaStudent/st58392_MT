import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebpageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_visibility(self):
        driver = self.driver
        
        try:
            # Verify header is present and visible
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")
            
            # Verify footer is present and visible
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
            
            # Verify navigation links are present and visible
            for link in ['http://localhost:8080/en/3-clothes', 
                         'http://localhost:8080/en/6-accessories', 
                         'http://localhost:8080/en/9-art']:
                nav_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
                self.assertTrue(nav_link.is_displayed(), f"Navigation link for {link} is not visible")
            
            # Verify input field (search) is present and visible
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 's')))
            self.assertTrue(search_input.is_displayed(), "Search input field is not visible")
            
            # Verify buttons are present and visible
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'login')]")))
            self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible")

            register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'registration')]")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")
            
            # Verify form elements and sections
            newsletter_form = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='http://localhost:8080/en/#blockEmailSubscription_displayFooterBefore']")))
            self.assertTrue(newsletter_form.is_displayed(), "Newsletter form is not visible")
            
            # Interact with the search input
            search_input.send_keys("Hummingbird")
            search_input.submit()

            # Confirm UI reacted visually by checking an element post search
            search_results_header = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Search results')]")))
            self.assertTrue(search_results_header.is_displayed(), "Search did not produce visible results")
        
        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()