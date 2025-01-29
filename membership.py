import time

from selenium.webdriver.common.by import By

from newwutilities.BaseClass import Baseclass


class Membership:

    def __init__(self, driver):
        self.driver = driver



    def membershipoption(self):
        self.driver.find_element(By.ID,"tm-148m").click()
        self.driver.find_element(By.LINK_TEXT,"Membership Overview").click()
        self.driver.find_element(By.XPATH,"//input[@id='ctl00_Body_rdoMemberStudent']").click()
        self.driver.find_element(By.CSS_SELECTOR,"#ctl00_Body_btnJoinNow").click()
        self.driver.find_element(By.XPATH,"//a[@title='Close']").click()
        self.driver.find_element(By.XPATH,"//input[@value='btnUseMailPayment']").click()
        self.driver.find_element(By.XPATH,"//input[@value='CREATE A QUOTE']").click()
        element = self.driver.find_element(By.CSS_SELECTOR,"#ctl00_body_ucPO_lHeader")
        assert element.text == "Mail Order"
        return print(element)






