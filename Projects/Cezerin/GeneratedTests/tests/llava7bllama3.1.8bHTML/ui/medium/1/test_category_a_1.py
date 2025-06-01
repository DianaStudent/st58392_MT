import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://example.com")  # Replace with your actual URL

    def test_homepage_elements_present(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category_a/category_a_1']"))
            )
            self.assertEqual(self.driver.title, "Example Domain")
            
            # Confirm presence of key interface elements
            navigation_links = self.driver.find_elements(By.TAG_NAME, 'nav')
            self.assertGreater(len(navigation_links), 0)
            
            inputs = self.driver.find_elements(By.TAG_NAME, 'input')
            self.assertGreater(len(inputs), 0)
            
            buttons = self.driver.find_elements(By.TAG_NAME, 'button')
            self.assertGreater(len(buttons), 0)
            
            banners = self.driver.find_elements(By.TAG_NAME, 'h1')
            self.assertGreater(len(banners), 0)
            
        except:
            self.fail("Some required elements are missing.")

    def test_interact_with_element(self):
        try:
            # Select a button to click
            button_to_click = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button button is-primary']"))
            )
            
            # Click the button and verify UI updates visually
            button_to_click.click()
            self.assertTrue(button_to_click.is_enabled())
            
        except:
            self.fail("Could not interact with an element.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])