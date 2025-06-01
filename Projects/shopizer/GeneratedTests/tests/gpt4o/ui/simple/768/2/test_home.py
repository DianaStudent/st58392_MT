import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class MyWebPageTest(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080")

    def test_home_page_elements(self):
        driver = self.driver

        try:
            # Wait for and verify header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area"))
            )
            
            # Verify main menu links
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Home").is_displayed())
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Tables").is_displayed())
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Chairs").is_displayed())

            # Verify accept cookies button
            cookies_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            self.assertTrue(cookies_button.is_displayed())

            # Verify login and register links
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Login").is_displayed())
            self.assertTrue(driver.find_element(By.LINK_TEXT, "Register").is_displayed())

            # Verify main product image and banner
            banner_image = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".site-blocks-cover img"))
            )
            self.assertTrue(banner_image.is_displayed())

            # Verify the subscription form
            subscribe_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 input[type='email']"))
            )
            self.assertTrue(subscribe_form.is_displayed())

            # Check if footer is present
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area"))
            )
            self.assertTrue(footer.is_displayed())
            
        except Exception as e:
            self.fail(f"UI Element missing: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()