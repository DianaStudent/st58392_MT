import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/9-art")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check the presence of input fields and buttons
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][name='s']")))
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.material-icons.search")))

            # Check the presence of banners
            banners = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Interact with the search input
            search_input.send_keys("poster")
            search_button.click()
            
            # Verify interaction updated the UI
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))

        except Exception as e:
            self.fail(f"UI elements are missing or interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()