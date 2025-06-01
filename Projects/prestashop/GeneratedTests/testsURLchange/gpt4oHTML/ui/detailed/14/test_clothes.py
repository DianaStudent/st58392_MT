import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/3-clothes')

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for page elements to be visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "menu")))

            # Check header elements
            header_logo = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/'] img")
            self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")

            # Check main navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu a.dropdown-item")
            expected_nav = [
                ('Clothes', 'http://localhost:8080/en/3-clothes'),
                ('Accessories', 'http://localhost:8080/en/6-accessories'),
                ('Art', 'http://localhost:8080/en/9-art')
            ]
            for link_text, link_url in expected_nav:
                link = driver.find_element(By.LINK_TEXT, link_text)
                self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")
                self.assertEqual(link.get_attribute('href'), link_url)

            # Check input fields and buttons
            search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search our catalog']")
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            cart_button = driver.find_element(By.CSS_SELECTOR, ".header .shopping-cart")
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

            # Interact with elements
            language_dropdown = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Language dropdown']")
            language_dropdown.click()

            language_options = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu a.dropdown-item")
            self.assertGreater(len(language_options), 0, "Language options are not available")

            # Footer elements
            footer = driver.find_element(By.ID, "footer")
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

        except Exception as e:
            self.fail(f"An element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()