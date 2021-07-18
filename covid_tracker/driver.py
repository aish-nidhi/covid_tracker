from controllers.UserController import UserController
from controllers.ZoneController import ZoneController
from controllers.AdminUserController import AdminUserController


usr_ctrlr = UserController()
zn_ctrlr = ZoneController()
adm_ctrlr = AdminUserController()

user_list = [
    {"name":"BR1", "pincode":100000, "number":1, "is_admin":False},
    {"name":"BR2", "pincode":100000, "number":2, "is_admin":False},
    {"name":"BR3", "pincode":100000, "number":3, "is_admin":False},
    {"name":"BR4", "pincode":100000, "number":4, "is_admin":False},
    {"name":"BR5", "pincode":100000, "number":5, "is_admin":False},
    {"name":"BR6", "pincode":200000, "number":6, "is_admin":False},
    {"name":"BR7", "pincode":200000, "number":7, "is_admin":False},
    {"name":"BR8", "pincode":200000, "number":8, "is_admin":False},
    {"name":"BR9", "pincode":200000, "number":9, "is_admin":False},
    {"name":"BR10", "pincode":200000, "number":10, "is_admin":False}
]

admin_list = [
    {"name":"admin1", "pincode":300000, "number":11, "is_admin":True},
    {"name":"admin2", "pincode":300000, "number":12, "is_admin":True},
]

import pdb;pdb.set_trace()

usr_ctrlr.add_user(user_list)
usr_ctrlr.add_user(admin_list)

usr_ctrlr.self_assessment(1, ["cold"], False, False)
usr_ctrlr.self_assessment(2, ["cold"], True, True)

adm_ctrlr.mark_result("admin1", "BR1", True)
adm_ctrlr.mark_result("admin1", "BR2", True)
adm_ctrlr.mark_result("admin1", "BR3", True)
adm_ctrlr.mark_result("admin1", "BR4", True)
adm_ctrlr.mark_result("admin1", "BR5", True)
adm_ctrlr.mark_result("admin1", "BR6", True)

usr_ctrlr.check_zone("BR1")
usr_ctrlr.check_zone("BR2")
usr_ctrlr.check_zone("BR3")
usr_ctrlr.check_zone("BR4")
usr_ctrlr.check_zone("BR5")
usr_ctrlr.check_zone("BR6")
usr_ctrlr.check_zone("BR7")
usr_ctrlr.check_zone("BR8")
usr_ctrlr.check_zone("BR9")
usr_ctrlr.check_zone("BR10")

adm_ctrlr.mark_result("admin1", "BR5", False)
usr_ctrlr.check_zone("BR5")

