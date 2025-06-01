import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopUI(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_shop_ui_elements(self):
        # Check header presence and visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        
        # Check navigation links presence and visibility
        nav_links = ["/category/tables", "/category/chairs"]
        for link in nav_links:
            self.assertTrue(self.driver.find_element(By.XPATH, f"//a[@href='{link}']").is_displayed())

        # Check main content presence and visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "main")))

        # Check footer presence and visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check required UI elements (buttons, links, form fields) presence and visibility
        ui_elements = [
            {"selector": By.XPATH, "value": "//button[@type='submit']", "displayed": True},
            {"selector": By.XPATH, "value": "//input[@name='username']", "displayed": True},
            {"selector": By.XPATH, "value": "//label[@for='username']", "displayed": True},
            {"selector": By.LINK_TEXT, "value": "Login", "displayed": True},
        ]
        for element in ui_elements:
            self.assertTrue(self.driver.find_element(element["selector"], element["value"]).is_displayed())

    def test_click_buttons(self):
        # Click button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        
        # Assert that UI reacts visually
        self.assertTrue(self.driver.find_element(By.XPATH, "//span[contains(text(), 'Please fill all fields')]"))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShopUI)
    unittest.TextTestRunner(verbosity=2).run(suite)