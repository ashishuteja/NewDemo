import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(10)


@pytest.fixture(scope="class")
def setup(request):
    driver.get("https://www.aapc.com")
    time.sleep(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

    #driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    #driver.get("https://rahulshettyacademy.com/angularpractice")
    #driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")






