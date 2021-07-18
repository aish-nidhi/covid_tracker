from constants import GREEN

class Zone(object):

    def __init__(self, pincode):
        self.pincode = pincode
        self.covid_cases = 0
        self.status = GREEN