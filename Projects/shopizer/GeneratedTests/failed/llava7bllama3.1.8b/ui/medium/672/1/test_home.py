from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def test_ui_components(self):
        # Check navigation links
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//nav//ul/li/a")))
        self.assertEqual(len(nav_links), 3)
        for link in nav_links:
            self.assertTrue(link.is_displayed())

        # Check banner
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='react-toast-notifications__container']")))
        self.assertTrue(banner.is_displayed())

        # Check buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button")))
        self.assertEqual(len(buttons), 3)
        for button in buttons:
            self.assertTrue(button.is_displayed())

    def test_button_click(self):
        # Click the "SHOP NOW" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary']"))).click()

        # Check that the UI updates visually
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='react-toast-notifications__container']")))
        self.assertTrue(banner.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()