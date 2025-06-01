from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Open the page
        self.driver.get("http://max/")

        try:
            # Confirm the presence of key interface elements: navigation links, inputs, buttons, banners
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='nav-links']")))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search-term']")))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

        except TimeoutException:
            self.fail("Timed out waiting for page to load")

        try:
            # Interact with one or two elements — e.g., click a button and check that the UI updates visually
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='results']")))

        except TimeoutException:
            self.fail("Timed out waiting for button click to update page")

if __name__ == '__main__':
    unittest.main()