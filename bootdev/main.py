class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        # dictionary indicating upgrade options of swords based on type
        upgrade_options = {
            'bronze': 'iron',
            'iron': 'steel'
        }
        # validation check to see if swords match and/or is apart of the given selection range
        if self.sword_type != other.sword_type or self.sword_type not in upgrade_options or other.sword_type not in upgrade_options:
            raise Exception("cannot craft")
        # return a new sword if validation checks out (i.e sword matches were found)
        return Sword(upgrade_options[self.sword_type])