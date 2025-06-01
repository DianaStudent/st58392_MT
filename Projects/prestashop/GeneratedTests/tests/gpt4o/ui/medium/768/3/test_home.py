import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify that the main nav links are present
        nav_links = [
            (By.LINK_TEXT, "Clothes"),
            (By.LINK_TEXT, "Accessories"),
            (By.LINK_TEXT, "Art"),
            (By.LINK_TEXT, "Sign in"),
            (By.LINK_TEXT, "Register"),
        ]

        for by, value in nav_links:
            try:
                wait.until(EC.visibility_of_element_located((by, value)))
            except:
                self.fail(f"Nav link '{value}' is not visible")

        # Verify the search bar is present
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-widgets")))
        except:
            self.fail("Search widget is not visible")

        # Verify the carousel is present
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
        except:
            self.fail("Carousel is not visible")

        # Interact with the carousel by clicking next button
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='right carousel-control']")))
            next_button.click()
        except:
            self.fail("Failed to interact with the carousel next button")

        # Verify no UI errors by checking element remains visible after interaction
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
        except:
            self.fail("Carousel is not visible after interaction")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()