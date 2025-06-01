import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for main navigation links
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except Exception as e:
            self.fail(f"Main navigation links are not present or not visible: {str(e)}")

        # Check for search input
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, 's')))
        except Exception as e:
            self.fail(f"Search input is not present or not visible: {str(e)}")

        # Check for Sign in button
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        except Exception as e:
            self.fail(f"Sign in button is not present or not visible: {str(e)}")
        
        # Check for Cart element
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'blockcart')]")))
        except Exception as e:
            self.fail(f"Cart element is not present or not visible: {str(e)}")

        # Check for banner
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='']/img[@class='img-fluid']")))
        except Exception as e:
            self.fail(f"Banner is not present or not visible: {str(e)}")

        # Interacting with a navigation link
        try:
            clothing_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            clothing_link.click()
            wait.until(EC.url_to_be("http://localhost:8080/en/3-clothes"))
        except Exception as e:
            self.fail(f"Failed to interact with navigation link or page did not load correctly: {str(e)}")

        # Verify no UI errors
        try:
            body_elem = driver.find_element(By.TAG_NAME, "body")
            self.assertNotIn("error", body_elem.text.lower())
        except Exception as e:
            self.fail(f"UI contains errors: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()