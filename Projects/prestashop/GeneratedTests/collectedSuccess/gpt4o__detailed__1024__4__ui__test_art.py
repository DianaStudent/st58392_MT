import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or visible.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not present or visible.")

        # Check navigation
        try:
            navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation is not present or visible.")

        # Check breadcrumb
        try:
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
        except:
            self.fail("Breadcrumb is not present or visible.")

        # Check product containers
        try:
            products = driver.find_elements(By.CLASS_NAME, "product-miniature")
            if len(products) != 7:
                self.fail("Number of product containers is incorrect.")
        except:
            self.fail("Product containers are not present or visible.")

        # Check search widget
        try:
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except:
            self.fail("Search widget is not present or visible.")

        # Check login link
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        except:
            self.fail("Login hyperlink is not present or visible.")

        # Check register link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Register hyperlink is not present or visible.")

        # Interact with quick view button & check reaction
        try:
            quick_view_buttons = driver.find_elements(By.CLASS_NAME, "quick-view")
            for button in quick_view_buttons:
                driver.execute_script("arguments[0].click();", button)
                # Check for modal or other visual change, may need additional checks here
                break
        except:
            self.fail("Quick view button interaction or reaction failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()