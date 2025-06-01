import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMax(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_max_interface_elements(self):
        # Open the page.
        self.driver.get("http://max/")

        # Confirm the presence of key interface elements: navigation links, inputs, buttons, banners
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#logo")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

        # Interact with one or two elements
        login_button = self.driver.find_element_by_css_selector("[href='login']")
        login_button.click()

        # Check that the UI updates visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-group")))

        # Verify that interactive elements do not cause errors in the UI
        self.assertEqual(self.driver.title, "Login")

    def test_search_page_elements(self):
        # Open the page.
        self.driver.get("http://max/search")

        # Confirm the presence of key interface elements: navigation links, inputs, buttons, banners
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#logo")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

        # Interact with one or two elements
        search_input = self.driver.find_element_by_css_selector("[name='q']")
        search_button = self.driver.find_element_by_css_selector("[type='submit']")
        search_input.send_keys("test")
        search_button.click()

        # Check that the UI updates visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-result")))

if __name__ == "__main__":
    unittest.main()