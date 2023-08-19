from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Orange:

    def __init__(self):
        self.url = "https://demo.nopcommerce.com/"
        self.driver = webdriver.Chrome()
        self.login_page = '//a[@href="/login?returnUrl=%2F"]'
        self.username = "Email"
        self.password = "Password"
        self.submit_button = '//button[@type="submit"]'

    def browse(self):
        self.driver.get(self.url)
        print(self.driver.title)
        print("The user is logged successfully")
        self.driver.maximize_window()
        sleep(2)

    def nopcommerce(self):
        sleep(2)
        loginpage_webelement = self.driver.find_element(By.XPATH, self.login_page)
        loginpage_webelement.click()
        sleep(2)

        username_webelement = self.driver.find_element(By.NAME, self.username)
        username_webelement.send_keys("vajay@gmail.com")

        password_webelement = self.driver.find_element(By.NAME, self.password)
        password_webelement.send_keys("Welcome@123")
        sleep(2)

        submit_webelement = self.driver.find_element(By.XPATH, self.submit_button)
        submit_webelement.click()
        sleep(2)


obj = Orange()
obj.browse()
obj.nopcommerce()
sleep(2)
