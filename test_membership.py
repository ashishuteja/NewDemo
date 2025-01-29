import time


from newwAAPCDEMO.membership import Membership
from newwAAPCDEMO.updateprofile import updateprofilee
from newwutilities.BaseClass import Baseclass


class Testmembership(Baseclass):

    def test_membership(self):
        membershp = Membership(self.driver)
        membershp.membershipoption()
        time.sleep(8)




