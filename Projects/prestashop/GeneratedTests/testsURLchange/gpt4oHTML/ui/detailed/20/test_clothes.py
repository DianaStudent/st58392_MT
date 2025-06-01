import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ClothingStoreUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.maximize_window()

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for the header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except:
            self.fail("Header missing")

        # Check for the footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except:
            self.fail("Footer missing")

        # Check for the navigation menu
        try:
            nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-nav')))
            self.assertTrue(nav.is_displayed(), "Navigation is not visible")
        except:
            self.fail("Navigation menu missing")

        # Check presence and visibility of input fields and buttons
        try:
            search_input = driver.find_element(By.CSS_SELECTOR, 'input[name="s"]')
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        except:
            self.fail("Search input missing")

        try:
            search_button = driver.find_element(By.CSS_SELECTOR, '.search')
            self.assertTrue(search_button.is_displayed(), "Search button is not visible")
        except:
            self.fail("Search button missing")

        # Check presence and visibility of links
        try:
            links = driver.find_elements(By.CSS_SELECTOR, 'a')
            self.assertTrue(all(link.is_displayed() for link in links), "Not all links are visible")
        except:
            self.fail("Links missing")

        # Interact with UI elements and check visual reaction
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')))
            clothes_link.click()
            self.assertIn('clothes', driver.current_url, "Failed to navigate to clothes section")
        except:
            self.fail("Unable to interact with Clothes link")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()