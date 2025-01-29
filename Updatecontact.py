from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UpdateContact:

    def __init__(self, driver):
        self.driver = driver

    def UpdateContact(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "lalit").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Preferences").click()
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='ctl00$Body$ddlRegion']"))
        dropdown.select_by_visible_text("NE")
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='ctl00$Body$ddlCountry']"))
        dropdown.select_by_index("6")

        #dropdown = Select(self.driver.find_element(By.XPATH,"//select[@name='ctl00$Body$ddlRegion']"))
        #dropdown.select_by_visible_text("NE")
        #dropdown = Select(self.driver.find_element(By.XPATH,"//select[@name='ctl00$Body$ddlCountry']"))
        #dropdown.select_by_index("7")


