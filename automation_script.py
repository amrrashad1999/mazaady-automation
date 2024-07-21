from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class MazaadyAutomation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Update this line if WebDriver is not in PATH
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_login_and_add_product(self):
        driver = self.driver
        driver.get('https://staging.mazaady.com/login')

        # Login
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')

        email_input.send_keys('tester@task.com')
        password_input.send_keys('11111111')
        login_button.click()

        # Wait for login to complete
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.profile-menu')))

        # Navigate to add product
        profile_menu = driver.find_element(By.CSS_SELECTOR, 'div.profile-menu')
        profile_menu.click()
        add_product_option = driver.find_element(By.XPATH, '//a[text()="Add Product"]')
        add_product_option.click()

        # Fill product details
        self.wait.until(EC.visibility_of_element_located((By.ID, 'main-image')))
        driver.find_element(By.ID, 'main-image').send_keys('/path/to/image.jpg')
        driver.find_element(By.ID, 'auction-details').send_keys('Details about the auction')
        driver.find_element(By.ID, 'policy').send_keys('Return policy details')

        # Check auction details
        estimation_value = driver.find_element(By.ID, 'estimation-value')
        buy_now_value = driver.find_element(By.ID, 'buy-now-value')
        self.assertGreater(float(buy_now_value.get_attribute('value')), float(estimation_value.get_attribute('value')))
        self.assertLessEqual(float(estimation_value.get_attribute('value')), float(buy_now_value.get_attribute('value')))

        # Choose auction type
        auction_type = driver.find_element(By.ID, 'auction-type')
        auction_type.click()
        auction_type.find_element(By.XPATH, '//option[text()="Your Auction Type"]').click()

        submit_button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        submit_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
