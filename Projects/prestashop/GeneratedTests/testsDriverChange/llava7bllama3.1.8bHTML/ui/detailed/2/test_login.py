import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_ui(self):
        # Load the page and ensure that structural elements are visible.
        self.driver.get("http://localhost:8080/en/")

        # Check the presence and visibility of input fields, buttons, labels, and sections.
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed())

        navigation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'nav')))
        self.assertTrue(navigation.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed())

        # Interact with key UI elements (e.g., click buttons).
        clothes_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Clothes']")))
        clothes_link.click()

        # Confirm that the UI reacts visually.
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'category-products')))

        # Assert that no required UI element is missing.
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'add-to-cart'))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'wishlist'))))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()