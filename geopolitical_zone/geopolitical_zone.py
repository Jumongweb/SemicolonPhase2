from enum import Enum


class GeopoliticalZone(Enum):
    NORTH_CENTRAL = ["Benue", "F.C.T", "kogi", "Kwara", "Nasarawa", "Niger", "Plateau"]
    NORTH_EAST = ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"]
    NORTH_WEST = ["Kaduna", "Kastina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"]
    SOUTH_EAST = ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"]
    SOUTH_SOUTH = ["Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "River"]
    SOUTH_WEST = ["Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"]

    @staticmethod
    def get_zone(state):
        for zone in GeopoliticalZone:
            if state.capitalize() in zone.value:
                return zone
        return None
