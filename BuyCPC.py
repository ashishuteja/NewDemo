import time

from selenium.webdriver.common.by import By


class CPC:
    def __init__(self, driver):
        self.driver = driver

    def BUYCPC(self):

        self.driver.find_element(By.XPATH,"//div[@class='header']/div[3]").click()
        self.driver.find_element(By.LINK_TEXT,"Training and Events").click()
        self.driver.find_element(By.ID,"tm-75A").click()
        self.driver.find_element(By.XPATH,"//a[@id='btnLink-akwz-akwz']").click()
        self.driver.find_element(By.XPATH,"//label[@for='ctl00_Body_rdoPreReqNo']").click()
        self.driver.find_element(By.XPATH,"//label[@for='ctl00_Body_rdoCodeBookNo']").click()
        self.driver.find_element(By.XPATH,"//a[@id='ctl00_Body_AddToCart']").click()
        element = self.driver.find_element(By.LINK_TEXT,"Continue Shopping")
        assert element.text == "Continue Shopping"
        time.sleep(10)