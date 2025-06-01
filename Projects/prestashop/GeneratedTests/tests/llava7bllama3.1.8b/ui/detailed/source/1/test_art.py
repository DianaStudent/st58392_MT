from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestWebpage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_webpage(self):
        # Given the home page URL:
        url = "http://localhost:8080/en/"
        
        # Load the webpage
        self.driver.get(url)
        
        # Wait for 20 seconds to load all elements on the webpage
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        try:
            # Check that the structural elements are visible (header, footer, navigation)
            self.assertTrue(self.driver.find_element(By.TAG_NAME, "header").is_displayed())
            self.assertTrue(self.driver.find_element(By.TAG_NAME, "footer").is_displayed())
            
            # Check that required UI elements exist and are visible
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Clothes").is_displayed())
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Accessories").is_displayed())
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Art").is_displayed())
            self.assertTrue(self.driver.find_element(By.ID, "loginButton").is_displayed())

        except AssertionError as e:
            # If any required element is missing, fail the test
            self.fail("Required UI elements are not visible.")

    def tearDown(self):
        # Close the browser window after testing
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()