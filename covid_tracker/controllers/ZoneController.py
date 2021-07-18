from models.zones import Zone


all_zones = {}


class ZoneController(object):

    def add_zones(self, pincode):
        if pincode not in self.all_zones.keys():
            zone = Zone(pincode)
            all_zones[pincode] = zone
        else:
            print("Zone Already Exists.")