import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageElements(unittest.TestCase):
    
    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.maximize_window()
    
    def test_ui_elements_present(self):
        driver = self.driver
        
        try:
            # Wait for and check the navigation links
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "HOME")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "CLOTHES")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "ACCESSORIES")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "ART")))
            
            # Wait for and check for the presence of key UI elements
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-banner"))) # Example banner
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".h1"))) # Page title
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[name='s']"))) # Search input
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-products-count"))) # Cart count
            
            # Verify that buttons are visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "MEN")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "WOMEN")))

            # Interact with the search box
            search_box = driver.find_element(By.CSS_SELECTOR, "#search_widget input[name='s']")
            search_box.click()
            search_box.send_keys("T-Shirts")
            search_box.submit()
            
            # Verify no UI errors
            WebDriverWait(driver, 20).until(EC.title_contains("Search"))
            
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()