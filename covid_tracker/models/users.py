class User(object):

    def __init__(self, name, number, pincode, is_admin=True):
        self.name = name
        self.number = number
        self.pincode = pincode
        self.is_admin = is_admin
        self.covid_result = False
        self.travel_history = False
        self.symptoms = []
        self.covid_contact = False
        self.risk_percent = 0
        self.tested_by = None