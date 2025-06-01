import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_shop_react_app(self):
        # Step 1: Open the page
        print("Opening the page...")

        # Step 2: Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.navbar-nav li"))
        )
        self.assertEqual(len(navigation_links), 5)
        print("Navigation links are present.")

        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        self.assertIsNotNone(form_fields)
        print("Form fields are present.")

        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.btn"))
        )
        self.assertEqual(len(buttons), 3)
        print("Buttons are present.")

        banners = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "banner"))
        )
        self.assertIsNotNone(banners)
        print("Banners are present.")

        # Step 3: Interact with one or two elements
        buttons[0].click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#loginButton"))
        )
        self.assertIsNotNone(self.driver.find_element(By.ID, "loginButton"))

        # Step 4: Verify that interactive elements do not cause errors in the UI
        form_fields.send_keys("test")
        buttons[1].click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#searchResults"))
        )
        self.assertIsNotNone(self.driver.find_element(By.ID, "searchResults"))

if __name__ == "__main__":
    unittest.main()