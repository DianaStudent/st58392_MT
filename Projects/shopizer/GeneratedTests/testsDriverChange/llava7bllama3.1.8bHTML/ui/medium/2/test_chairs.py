import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_verify_elements_present(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
        )
        self.assertGreater(len(navigation_links), 0)

        # Inputs and buttons
        input_fields = self.driver.find_elements(By.CSS_SELECTOR, "input")
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
        self.assertGreater(len(input_fields), 0)
        self.assertGreater(len(buttons), 0)

        # Banners
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='react-toast-notifications__container']"))
        )
        self.assertIsNotNone(banner)

    def test_interact_with_button(self):
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        )
        button.click()
        # Verify UI updates visually
        banner = self.driver.find_element(By.XPATH, "//div[@class='react-toast-notifications__container']")
        self.assertIsNotNone(banner)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()