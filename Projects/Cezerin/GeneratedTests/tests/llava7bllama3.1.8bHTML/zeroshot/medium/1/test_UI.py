import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestInterfaceElements(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://localhost:3000")
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def test_interface_elements(self):
        # Confirm the presence of key interface elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav")))
        nav_links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in nav_links:
            if link.text not in ["Home", "Category A", "Category A-1"]:
                self.fail(f"Unknown navigation link: {link.text}")

        input_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'input-field')))
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Interact with one or two elements — e.g., click a button and check that the UI updates visually.
        button.click()

        # Verify that interactive elements do not cause errors in the UI.
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='error-message']")))
        except TimeoutException:
            pass
        else:
            self.fail("Error message is displayed")

if __name__ == "__main__":
    unittest.main()