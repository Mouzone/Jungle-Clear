
#each indice in each table represents how much resource is given at that camp's level
class Camp():
    camps = {
        "Gromp":{
            "gold": [80],
            "xp": [120, 123, 129, 144, 156, 174]
        },
        "Blue":{
            "gold": [90],
            "xp": [95, 97.38, 102.13, 114, 123.5, 137.75]
        },
        "Wolves":{
            "Big": {
                "gold": [55],
                "xp": [50, 51.25, 53.75, 60, 65, 72.5]
            },
            "Small": {
                "gold": [13],
                "xp": [15, 15.38, 16.13, 18, 19.5, 21.75]
            }
        },
        "Raptors":{
            "Big": {
                "gold_table": [35],
                "xp_table": [20, 20.5, 21.5, 24, 26, 29]
            },
            "Small": {
                "gold": [8],
                "xp": [10, 10.25, 10.75, 12, 13, 14.5]
            }
        },
        "Red":{
            "gold": [90],
            "xp": [95, 97.38, 102.13, 114, 123.5, 137.75]
        },
        "Krugs":{
            "Big":{
                "gold": [15],
                "xp": [15, 15.38, 16.13, 18, 19.5, 21.75]
            },
            "Medium":{
                "gold": [10],
                "xp": [10, 10.25, 10.75, 12, 13, 14.5]
            },
            "Small":{
                "gold": [14],
                "xp": [10, 10.25, 10.75, 12, 13, 14.5]
            }
        },
        "Scuttle":{
            "gold": [100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 210, 220],
            "xp": [55, 57.75, 60.5, 63.25, 66, 68.75, 71.5, 74.25, 77, 82.5, 88, 93.5, 99, 104.5, 110, 115.5, 121]
        }
    }

    def get_camp_resource(camp, resource):
        #creeps_clear is a list [0,2] means 0 big 2 small
        #big is a boolean
        #small is a number
        #big and small is optional, if not specified kills whole camp
        total = 0
        if camp == "Gromp":
            total = camps["Gromp"][resource][0]
        elif camp == "Blue":
            total = camps["Blue"][resource][0]
        elif camp == "Wolves":
            total = camps["Wolves"]["Big"][resource][0] + 2*camp["Wolves"]["Small"][resource][0]
        elif camp == "Raptors":
            total = camps["Raptors"]["Big"][resource][0] + 5*camp["Raptors"]["Small"][resource][0]
        elif camp == "Red":
            total = camps["Red"][resource][0]
        elif camp =="Krugs":
            total = camps["Krugs"]["Big"][resource][0] + camps["Krugs"]["Medium"][resource][0] + 6 * camps["Krugs"]["Big"][resource][0]
        else:
            total = camps["Scuttle"][resource][0]
        level_up_camps(camp, resource)
        return gold
        #might need a special function for krugs, ancient krug on death spawns 4 minis, medium krug on death spawns 2 minis

    def level_up_camps(camp, resource):
        if camp == "Krugs" or camp == "Raptors" or camp == "Wolves":
            for creep in camps[camp]:
                if len(camps[camp][creep][resource]) == 1:
                    return 
                camps[camp][creep][resource] = camps[camp][creep][resource][1:]
        else:
            if len(camps[camp][resource]) == 1:
                    return 
            camps[camp][resource] = camps[camp][resource][1:]

class Champion():
    champion_xp = 0
    champion_gold = 0
    champion_level = 1
    xp_required = 280

    def get_champion_gold(self):
        return self.champion_gold

    def get_champion_xp(self):
        return self.champion_xp

    def get_champion_level(self):
        return self.champion_level

    def increment_champion_gold(self, increment):
        champion_gold += increment

    def increment_exp(self, increment):
        champion_xp += incremenet
        self.increment_level()
    
    def increment_level(self):
        if champion_xp // xp_required == 1:
            champion_level += 1
            xp_required += 100
    
    def kill_camp(self, camp):
        self.increment_champion_gold(camp.get_camp_gold())
        self.increment_exp(camp.get_camp_xp())

