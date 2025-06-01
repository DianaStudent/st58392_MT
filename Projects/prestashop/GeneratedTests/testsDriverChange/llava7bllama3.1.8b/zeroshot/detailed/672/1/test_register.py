import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_registration_flow(self):
        # 1. Open the homepage
        # No action needed here

        # 2. Click the login link from the top navigation.
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/login']"))).click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/register']"))).click()

        # 4. Fill in the following fields using credentials:
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='gender']"))).send_keys("1")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstname']"))).send_keys("Test")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastname']"))).send_keys("User")
        email = f"test_{self.getRandomString()}@user.com"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys("test@user1")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='birthday']"))).send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # Assume there are check boxes with the following names:
        checkboxes = ["privacy", "newsletter", "terms"]
        for checkbox in checkboxes:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//input[@name='{checkbox}']"))).click()

        # 6. Submit the registration form.
        driver.find_element(By.NAME, 'submit').click()

        # 7. Wait for the redirect after login.
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='nav-link']")))

        # 8. Confirm that login was successful by checking that:
        self.assertEqual("Sign out", driver.find_element(By.XPATH, "//a[@class='nav-link']").text)
        self.assertEqual(email, driver.find_element(By.XPATH, "//span[@class='navbar-text']").text)

    def getRandomString(self):
        import random
        return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(10))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()