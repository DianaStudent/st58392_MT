import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestEcommerceSite(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        # Wait for the page to load and check if navigation links are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='nav']/li"))
        )

        # Check that inputs, buttons, banners are present in the UI
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "input")), 7)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 5)
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='banner']").is_displayed())

    def test_interaction(self):
        # Click on the 'Clothes' link
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/en/3-clothes']"))
        ).click()

        # Check if the page title has changed
        self.assertEqual(self.driver.title, "Ecommerce | Clothes")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()