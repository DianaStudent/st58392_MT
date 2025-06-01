import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestKeyUIElementsOnDemoPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check navigation visibility
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation bar is not visible.")

        # Check search input visibility
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible.")

        # Check key links visibility
        links_to_check = [
            ("Contact us", "http://localhost:8080/en/contact-us"),
            ("Sign in", "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F"),
            ("Cart", "#_desktop_cart")
        ]
        
        for text, href in links_to_check:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{href}']")))
            self.assertTrue(element.is_displayed(), f"Link '{text}' is not visible.")

        # Check sample product presence
        product_sample = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product")))
        self.assertTrue(product_sample.is_displayed(), "Sample product is not visible.")

        # Check dropdown language selector
        language_selector = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector")))
        self.assertTrue(language_selector.is_displayed(), "Language selector is not visible.")

        # Interact with search input (simulate typing)
        search_input.send_keys("Sample product")
        search_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".material-icons.search")))
        search_btn.click()

        # Ensure the page reacts (dummy check to demonstrate interaction-react scenario)
        page_footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-footer")))
        self.assertTrue(page_footer.is_displayed(), "Page footer is not visible after interaction.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()