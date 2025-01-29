import time

from newwAAPCDEMO.BuyCPC import CPC
from newwAAPCDEMO.conftest import driver
from newwutilities.BaseClass import Baseclass


class TestCPC(Baseclass):


    def test_CPC(self):
        cpc_obj = CPC(self.driver)
        cpc_obj.BUYCPC()
        time.sleep(5)
