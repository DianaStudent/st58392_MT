from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header is visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except Exception as e:
            self.fail(f"Header not found or not visible: {str(e)}")
            
        # Check main links in the top menu
        links = [
            ("Home", "http://localhost:8080/en/"),
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
        ]
        for link_text, link_url in links:
            try:
                link = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, f"//a[@href='{link_url}']"))
                )
                self.assertEqual(link.text, link_text, f"Link text does not match for {link_url}")
            except Exception as e:
                self.fail(f"Link {link_text} not found or not visible: {str(e)}")
        
        # Check for search bar
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertTrue(search_bar.is_displayed(), "Search bar is not visible")
        except Exception as e:
            self.fail(f"Search bar not found or not visible: {str(e)}")

        # Check for filters section
        try:
            filters_section = wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))
            self.assertTrue(filters_section.is_displayed(), "Filters section is not visible")
        except Exception as e:
            self.fail(f"Filters section not found or not visible: {str(e)}")

        # Check for product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertTrue(product_list.is_displayed(), "Product list is not visible")
        except Exception as e:
            self.fail(f"Product list not found or not visible: {str(e)}")
        
        # Check sign in link
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(@href, '/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art')]")
            ))
            self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible")
        except Exception as e:
            self.fail(f"Sign in link not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()