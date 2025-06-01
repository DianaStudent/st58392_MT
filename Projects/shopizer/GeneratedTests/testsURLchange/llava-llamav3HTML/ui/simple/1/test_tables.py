import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import WebDriverWait

class TestMainUIComponents(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver with the appropriate browser and capabilities.
        manager = ChromeDriverManager('chromedriver')
        driver = webdriver.Chrome(driver_path=manager.install())
        
        # Navigate to the home page.
        self.driver.get("http://localhost/")
    
    def tearDown(self):
        # Close the browser after the test.
        self.driver.quit()
    
    # Test that the main UI components are present, exist and visible.
    def testMainUIComponents(self):
        # Check if headers are present
        self.assertTrue(
            self.driver.find_elements_by_tag_name("header"),
            "Headers not found"
        )
        
        # Check if buttons are present
        self.assertTrue(
            self.driver.find_elements_by_tag_name("button"),
            "Buttons not found"
        )
        
        # Check if links are present
        self.assertTrue(
            self.driver.find_elements_by_tag_name("a"),
            "Links not found"
        )
        
        # Check if form fields are present
        self.assertTrue(
            self.driver.find_elements_by_tag_name("input"),
            "Form fields not found"
        )
        
        # Wait for the UI to be fully loaded, up to 20 seconds.
        WebDriverWait(self.driver, 20).until(
            lambda x: x.title == "Home - The Complete Solution for the Tableware Industry"
        )

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestMainUIComponents)
    runner = unittest.TextTestRunner(suite)
    runner.run()