
#each indice in each table represents how much resource is given at that camp's level
#add 15xp for large camps, and 12 xp for small camps
class Jungle():
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
                "gold": [35],
                "xp": [20, 20.5, 21.5, 24, 26, 29]
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
    def __init__(self):
    #increment all the xps by 15 or 12 depending on if it is large camp or small respectively
        for camp in camps:
            if camp == "Krugs" or camp == "Raptors" or camp == "Wolves":
                for creep in Jungle.camps[camp]:
                    if creep == "Big":
                        self.camps[camp][creep]['xp'] = [x + 15 for x in self.camps[camp][creep]['xp']]
                    else:
                        self.camps[camp][creep]['xp'] = [x + 12 for x in self.camps[camp][creep]['xp']]
            else:
                self.camps[camp]['xp'] = [x + 15 for x in self.camps[camp]['xp']]

    @staticmethod
    def get_camp_resource(camp, resource):
        total = 0
        if camp == "Gromp":
            total = Jungle.camps["Gromp"][resource][0]
        elif camp == "Blue":
            total = Jungle.camps["Blue"][resource][0]
        elif camp == "Wolves":
            total = Jungle.camps["Wolves"]["Big"][resource][0] + 2 * Jungle.camps["Wolves"]["Small"][resource][0]
        elif camp == "Raptors":
            total = Jungle.camps["Raptors"]["Big"][resource][0] + 5 * Jungle.camps["Raptors"]["Small"][resource][0]
        elif camp == "Red":
            total = Jungle.camps["Red"][resource][0]
        elif camp == "Krugs":
            total = Jungle.camps["Krugs"]["Big"][resource][0] + Jungle.camps["Krugs"]["Medium"][resource][0] + 6 * Jungle.camps["Krugs"]["Small"][resource][0]
        else:
            total = Jungle.camps["Scuttle"][resource][0]
        Jungle.level_up_camps(camp, resource)
        return total

    @staticmethod
    def level_up_camps(camp, resource):
        if camp == "Krugs" or camp == "Raptors" or camp == "Wolves":
            for creep in Jungle.camps[camp]:
                if len(Jungle.camps[camp][creep][resource]) == 1:
                    return
                Jungle.camps[camp][creep][resource] = Jungle.camps[camp][creep][resource][1:]
        else:
            if len(Jungle.camps[camp][resource]) == 1:
                return
            Jungle.camps[camp][resource] = Jungle.camps[camp][resource][1:]

class Champion:
    champion_xp = 150
    champion_gold = 0
    champion_level = 1
    xp_required = 280

    jungle = Jungle()

    def get_champion_gold(self):
        return self.champion_gold

    def get_champion_xp(self):
        return self.champion_xp

    def get_champion_level(self):
        return self.champion_level

    def increment_champion_gold(self, increment):
        self.champion_gold += increment

    def increment_exp(self, increment):
        self.champion_xp += increment
        self.increment_level()

    def increment_level(self):
        if self.champion_xp // self.xp_required == 1:
            self.champion_level += 1
            self.xp_required += 100

    def kill_camp(self, camp):
        self.increment_champion_gold(self.jungle.get_camp_resource(camp, "gold"))
        self.increment_exp(self.jungle.get_camp_resource(camp, "xp"))

def main():
    champion = Champion()
    #take input in form of string while string is not End
    #on end give xp and gold
    #else keep putting camps in
    while True:
        user_input = input("Enter Camp (type 'end' to stop): ")
        
        if user_input.lower() == "end":
            break
        
        champion.kill_camp(user_input)
    
    print(champion.get_champion_gold())
    print(champion.get_champion_level())
    print(champion.get_champion_xp())

if __name__ == "__main__":
    main()