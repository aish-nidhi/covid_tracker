from models.users import User
from controllers.ZoneController import all_zones, ZoneController


all_users = {}


class UserController(object):

    def add_user(self, user_list):
        self.users = {}
        try:
            count = 0
            for each in user_list:
                print(each)
                if each.number not in all_users.keys():
                    usr = User(each.name, each.number, each.pincode, each.is_admin)
                    if count == 0:
                        self.users = {each.number: usr}
                        count += 1
                    else:
                        self.users[each.number] = usr
                    if each.pincode in all_zones.keys():
                        ZoneController().add_zones(each.pincode)
                else:
                    print("User with number {0}, Already Exists.".format(each.number))
        except Exception:
            print("User Registration Unsuccessful")

        print("Successfully Registered.", self.users)
        return self.users

    def list_users(self, number=None):
        if number:
            user = all_users.get(number, None)
            if user:
                print("Name: {0}\nCovid Result: {1}\nRisk Percent: {2}".format(user.name, user.covid_result, user.risk_percent))
            else:
                print("User not found.")
        else:
            print("Invalid Request.")

    def check_zone(self, number=None):
        if number:
            user = all_users.get(number, None)
            if user:
                if user.pincode in all_zones.keys():
                    zone = all_zones[user.pincode]
                    print("Zone Status: {0}, Number of Cases: {1}".format(zone.status, zone.covid_cases))
            else:
                print("User not found.")
        else:
            print("Invalid Request.")

    def self_assessment(self, number, symptoms, travel_history, covid_contact):
        if len(symptoms) < 1 and not travel_history and not covid_contact:
            all_users[number].travel_history = travel_history
            all_users[number].covid_contact = covid_contact
            all_users[number].symptoms = symptoms
            all_users[number].risk_percent = 5
        elif len(symptoms) == 1 and (travel_history or covid_contact):
            all_users[number].travel_history = travel_history
            all_users[number].covid_contact = covid_contact
            all_users[number].symptoms = symptoms
            all_users[number].risk_percent = 50
        elif len(symptoms) == 2 and (travel_history or covid_contact):
            all_users[number].travel_history = travel_history
            all_users[number].covid_contact = covid_contact
            all_users[number].symptoms = symptoms
            all_users[number].risk_percent = 75
        elif len(symptoms) > 2 and (travel_history or covid_contact):
            all_users[number].travel_history = travel_history
            all_users[number].covid_contact = covid_contact
            all_users[number].symptoms = symptoms
            all_users[number].risk_percent = 95

        return all_users[number].risk_percent