from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class DemoUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check header
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        
            # Check Navigation menu links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        
            # Check sign in button
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))

            # Check search field
            self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Check Carousel
            self.wait.until(EC.visibility_of_element_located((By.ID, "carousel")))

            # Check Popular Products section
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Popular Products')]")))

            # Check Featured Products section
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'On sale')]")))

            # Check New Products section
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'New products')]")))

            # Check footer
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()