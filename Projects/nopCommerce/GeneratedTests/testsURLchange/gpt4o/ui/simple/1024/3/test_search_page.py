import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUIElements(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode.
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Check header elements
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))

            # Check for logo
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img")))

            # Check search box
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-box-button")))

            # Check top menu
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".top-menu.notmobile")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='top-menu notmobile']/li/a[text()='Home page']")))

            # Check search form
            self.wait.until(EC.visibility_of_element_located((By.ID, "q")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button-1.search-button")))

            # Check footer
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()