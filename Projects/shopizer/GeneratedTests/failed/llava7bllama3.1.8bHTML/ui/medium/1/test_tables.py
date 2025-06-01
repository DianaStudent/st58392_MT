from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestShopWebsite(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost/")

    def test_shop_website_elements(self):
        # Step 1: Open the page
        assert "Home" in self.driver.title

        # Step 2: Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navbarSupportedContent li a")))
        inputs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']")))
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[type='submit']")))

        banners = self.driver.find_elements(By.CSS_SELECTOR, ".carousel-caption")

        # Step 3: Interact with one or two elements
        buttons[0].click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbarSupportedContent li a.active")))

    def test_shop_website_interactive_elements(self):
        # Step 4: Verify that interactive elements do not cause errors in the UI
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navbarSupportedContent li a")))
        for link in navigation_links:
            link.click()
            self.assertEqual(link.get_attribute("class"), "nav-link active")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()