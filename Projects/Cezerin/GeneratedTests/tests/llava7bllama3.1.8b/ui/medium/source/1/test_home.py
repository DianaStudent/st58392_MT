import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUiElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link"))
        )
        self.assertEqual(len(navigation_links), 3)

        # Inputs and form fields (assuming this is for a search bar)
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='search']")
        ))
        self.assertIsNotNone(search_input)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn")
        ))
        self.assertEqual(len(buttons), 2)
        buttons[0].click()  # Assuming the first button is clickable

        # Banners
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".banner")
        ))
        self.assertIsNotNone(banners)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()