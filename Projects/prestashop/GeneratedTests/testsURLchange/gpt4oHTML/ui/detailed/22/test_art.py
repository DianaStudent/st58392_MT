import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of main sections
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            main = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "main")))

            # Check presence of navigation items
            nav_clothes = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            nav_accessories = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            nav_art = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Check for input fields and buttons
            search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @placeholder='Search our catalog']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit' and @value='Subscribe']")))

            # Interact with elements - click on 'Art' in navigation
            nav_art.click()

            # Confirm UI reaction - check if the page title changed to "Art"
            art_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Art']")))
        
        except Exception as e:
            self.fail(f"Required UI elements are missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()