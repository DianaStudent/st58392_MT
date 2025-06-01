import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestHomePage(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000")  # assuming the page is running on localhost

    def tearDown(self):
        self.driver.quit()

    def test_home_page_elements(self):
        # Confirm navigation links are present
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav li"))
        )
        self.assertGreater(len(nav_links), 0)

        # Check that banner is present and visible
        banner = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#home-slider .slide8.jpg"))
        )
        self.assertTrue(banner.is_displayed())

        # Find all form fields
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input"))
        )

        # Check that buttons are present and visible
        buttons = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button"))
        )
        self.assertGreater(len(buttons), 0)

        # Interact with one button (e.g. click the first button)
        buttons[0].click()

        # Wait for UI to update
        time.sleep(1)  # add some delay to see if UI has updated

        # Check that no JavaScript errors occurred
        self.driver.get_screenshot_as_file("screenshot.png")  # save screenshot
        js_errors = self.driver.find_element_by_css_selector('#js-error')
        self.assertFalse(js_errors)

    def test_navigation_links(self):
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav li"))
        )
        for link in nav_links:
            self.assertTrue(link.is_enabled())
            link.click()
            time.sleep(1)  # add some delay
            self.assertEqual(self.driver.current_url, link.get_attribute('href'))
            self.driver.back()

if __name__ == "__main__":
    unittest.main()