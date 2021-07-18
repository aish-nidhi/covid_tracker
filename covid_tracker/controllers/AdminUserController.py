from controllers.UserController import all_users, all_zones


class AdminUserController(object):

    def mark_result(self, adminId, uid, result):
        if uid in all_users.keys():
            all_users[uid].tested_by = adminId
            all_users[uid].covid_result = True
            all_zones[all_users[uid].pincode].covid_cases += 1
            print("Updated Result for User {0}".format(all_users[uid].name))
        else:
            print("Invalid User")