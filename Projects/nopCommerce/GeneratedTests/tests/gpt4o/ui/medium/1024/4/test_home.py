import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))

            # Verify navigation links
            for link in ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link)))

            # Verify search box
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertTrue(search_box.is_displayed(), "Search box is not displayed!")

            # Verify banner images
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "slider-img")))

            # Interact with search box
            search_box.send_keys("phone")
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))).click()
            WebDriverWait(driver, 10).until(lambda d: "q=phone" in d.current_url)

        except Exception as e:
            self.fail(f"Failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()