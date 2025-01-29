import time

from newwAAPCDEMO.updateprofile import updateprofilee
from newwutilities.BaseClass import Baseclass


class TestUpdateProfile(Baseclass):



    def test_updatepro(self):
        update = updateprofilee(self.driver)
        update.updatepro()
        update.clickupdatebutton()
        time.sleep(10)