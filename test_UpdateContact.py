import time

from newwAAPCDEMO.Updatecontact import UpdateContact
from newwAAPCDEMO.conftest import driver
from newwutilities.BaseClass import Baseclass


class TestUpdateContact(Baseclass):

    def test_updateContact(self):
        updatecntact = UpdateContact(self.driver)
        updatecntact.UpdateContact()
        time.sleep(10)