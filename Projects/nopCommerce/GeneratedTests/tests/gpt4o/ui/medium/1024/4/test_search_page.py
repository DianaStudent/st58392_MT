import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebUITests(unittest.TestCase):
    
    def setUp(self):
        # Setup the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
    
    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Wait for and verify key UI elements
            # Header links: Home, New products, Search, My account, Blog, Contact us
            header_links = [
                '/html/body/div[1]/div/ul/li[1]/a',
                '/html/body/div[1]/div/ul/li[2]/a',
                '/html/body/div[1]/div/ul/li[3]/a',
                '/html/body/div[1]/div/ul/li[4]/a',
                '/html/body/div[1]/div/ul/li[5]/a',
                '/html/body/div[1]/div/ul/li[6]/a'
            ]
            
            for link_xpath in header_links:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, link_xpath))
                )
                self.assertTrue(element.is_displayed(), "Header link not displayed")
            
            # Search form elements
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "q"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input box not displayed")
            
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="small-search-box-form"]/button'))
            )
            self.assertTrue(search_button.is_displayed(), "Search button not displayed")
            
            # Footer links check (example for one block)
            footer_links = [
                '/html/body/div[2]/div/div[1]/ul/li[1]/a',
                '/html/body/div[2]/div/div[1]/ul/li[2]/a',
                '/html/body/div[2]/div/div[1]/ul/li[3]/a'
            ]
            
            for link_xpath in footer_links:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, link_xpath))
                )
                self.assertTrue(element.is_displayed(), "Footer link not displayed")
            
            # Interact with the search button
            search_button.click()
            # Verify the page has started a search or loaded a result page
            search_page_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "page-title"))
            )
            self.assertTrue(search_page_title.is_displayed(), "Search page title not displayed after click")
        
        except Exception as e:
            self.fail(f"UI test failed: {str(e)}")
    
    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()