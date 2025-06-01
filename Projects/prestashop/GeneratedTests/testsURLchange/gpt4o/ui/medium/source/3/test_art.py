import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Test presence of main navigation elements
        try:
            # Home Link
            self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home"))))
            
            # Clothes Link
            self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))))
            
            # Accessories Link
            self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))))
            
            # Art Link
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            self.assertTrue(art_link)

            # Login Link
            self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sign in')]"))))

            # Search Input
            self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']"))))

            # Cart Button
            self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.shopping-cart"))))
        
        except Exception as e:
            self.fail(f"Required element is missing: {e}")

        # Interaction test
        try:
            # Click the "Art" link
            art_link.click()

            # Verify the current page is "Art"
            self.assertTrue(self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Art")))

        except Exception as e:
            self.fail(f"UI interaction failed: {e}")

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()