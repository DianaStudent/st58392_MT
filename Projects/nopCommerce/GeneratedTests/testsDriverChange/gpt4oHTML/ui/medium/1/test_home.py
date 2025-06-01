import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://max/"

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_and_interaction(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url)

        # Confirm presence of key interface elements
        try:
            # Verify Navigation Links
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page"))))
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products"))))
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search"))))

            # Verify Header Elements
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header"))))
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links"))))

            # Verify Form Field and Button
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))

            # Interact with elements
            search_input.clear()
            search_input.send_keys("test")
            search_button.click()

            # Confirm no UI errors after interaction
            notification_bar = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
            self.assertTrue(notification_bar.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to missing required element or error: {str(e)}")

if __name__ == "__main__":
    unittest.main()