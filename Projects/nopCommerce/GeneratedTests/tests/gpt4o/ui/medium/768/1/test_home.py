import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
    
    def test_home_page_ui_elements(self):
        driver = self.driver
        
        # Verify header menu links
        expected_links_texts = [
            "Home page", "New products", "Search", "My account", "Blog", "Contact us"
        ]
        for text in expected_links_texts:
            try:
                link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, text))
                )
                self.assertTrue(link.is_displayed(), f"{text} link is not displayed")
            except Exception as e:
                self.fail(f"{text} link: {str(e)}")
        
        # Verify search input and button
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input is not displayed")
            
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            self.assertTrue(search_button.is_displayed(), "Search button is not displayed")
        except Exception as e:
            self.fail(f"Search input and button: {str(e)}")
        
        # Verify banner images
        try:
            banner_img1 = driver.find_element(By.CSS_SELECTOR, "img[src*='banner_1.webp']")
            self.assertTrue(banner_img1.is_displayed(), "Banner 1 is not displayed")

            banner_img2 = driver.find_element(By.CSS_SELECTOR, "img[src*='banner_2.webp']")
            self.assertTrue(banner_img2.is_displayed(), "Banner 2 is not displayed")
        except Exception as e:
            self.fail(f"Banner images: {str(e)}")
        
        # Interact with 'Search' button
        try:
            search_input.send_keys("Test")
            search_button.click()
            WebDriverWait(driver, 20).until(EC.url_contains("search?q=Test"))
        except Exception as e:
            self.fail(f"Search interaction: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()