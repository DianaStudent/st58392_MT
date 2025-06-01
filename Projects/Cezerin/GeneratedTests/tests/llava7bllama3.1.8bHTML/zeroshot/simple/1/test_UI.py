import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")

    def test_main_ui_components(self):
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        self.assertEqual(self.driver.find_element(By.XPATH, "//h1").text, "Home Page")

        # Check that these elements exist and are visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='checkout-button button is-primary']"))
        )
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[@class='checkout-button button is-primary']").is_displayed())

        # Check that the link to category_a URL exists and is visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        self.assertTrue(self.driver.find_element(By.XPATH, "//a[@href='/category-a']").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()