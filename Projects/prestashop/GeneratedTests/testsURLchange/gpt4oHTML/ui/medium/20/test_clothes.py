import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Confirm the presence of main navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        except Exception as e:
            self.fail("Main navigation links are not present: " + str(e))

        # Interact with one element (click 'Clothes' link)
        try:
            clothes_link.click()
            clothes_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Clothes']")))
        except Exception as e:
            self.fail("Interaction with 'Clothes' link failed or did not update UI as expected: " + str(e))

        # Confirm additional elements on the new page
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']")))
            cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header']//i[@class='material-icons shopping-cart']")))
            wishlist_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'wishlist-button-add')]")))
        except Exception as e:
            self.fail("Additional UI elements are missing on the 'Clothes' page: " + str(e))

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()