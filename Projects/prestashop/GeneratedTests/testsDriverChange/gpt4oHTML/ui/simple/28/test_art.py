import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
    
    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
            
            # Main links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertEqual(home_link.get_attribute('href'), "http://localhost:8080/en/")
            
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.assertEqual(clothes_link.get_attribute('href'), "http://localhost:8080/en/3-clothes")
            
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.assertEqual(accessories_link.get_attribute('href'), "http://localhost:8080/en/6-accessories")
            
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            self.assertEqual(art_link.get_attribute('href'), "http://localhost:8080/en/9-art")
            
            # Login and Register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertEqual(login_link.get_attribute('href'), "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
            
            register_link = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Create account")))
            self.assertEqual(register_link.get_attribute('href'), "http://localhost:8080/en/registration")
            
            # Cart and Search Widgets
            cart_widget = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".blockcart")))
            self.assertTrue(cart_widget.is_displayed(), "Cart widget is not visible")
            
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.assertTrue(search_widget.is_displayed(), "Search widget is not visible")

            # Footer and newsletter
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
            
            newsletter_section = driver.find_element(By.ID, "block_newsletter_label")
            self.assertTrue(newsletter_section.is_displayed(), "Newsletter section is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()