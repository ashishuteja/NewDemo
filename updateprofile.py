import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class updateprofilee:

    def __init__(self, driver):
        self.driver= driver

    def updatepro(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"lalit").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Preferences").click()
        self.driver.find_element(By.XPATH,"//div[@id='headingSix'] ").click()
        dropdown = Select(self.driver.find_element(By.ID,"ddlEducation"))
        dropdown.select_by_visible_text("High School")
        dropdown1 = self.driver.find_element(By.ID,"ddlInstitutes")
        select = Select(dropdown1)
        select.select_by_index(3)
        checkbox = self.driver.find_elements(By.XPATH,"//div[@class='chapters-list']//input[@type='checkbox']")
        print(len(checkbox))
        for check in checkbox:
            if check.get_attribute("name") == "ctl00$Body$cblNonAAPCCertifications$17":
                check.click()

    def clickupdatebutton(self):
        self.driver.find_element(By.XPATH,"(//input[@type='submit'])[5]").click()
        element = self.driver.find_element(By.CSS_SELECTOR,"#ctl00_Body_spanMsgEducationCert")
        assert element.text == "Your profile has been updated"
        time.sleep(10)