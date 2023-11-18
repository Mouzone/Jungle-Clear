
#each indice in each table represents how much resource is given at that camp's level
camps = {
        "Gromp":{
            gold_table: [80],
            xp_table: [120, 123, 129, 144, 156, 174]
        },
        "Blue":{
            gold_table: [90],
            xp_table: [95, 97.38, 102.13, 114, 123.5, 137.75]
        },
        "Wolves":{
            "Big": {
                gold_table: [55],
                xp_table: [50, 51.25, 53.75, 60, 65, 72.5]
            },
            "Small": {
                gold_table: [13],
                xp_table: [15, 15.38, 16.13, 18, 19.5, 21.75]
            }
        },
        "Raptors":{
            "Big": {
                gold_table: [35],
                xp_table: [20, 20.5, 21.5, 24, 26, 29]
            },
            "Small": {
                gold_table: [8],
                xp_table: [10, 10.25, 10.75, 12, 13, 14.5]
            }
        },
        "Red Buff":{
            gold_table: [90],
            xp_table: [95, 97.38, 102.13, 114, 123.5, 137.75]
        },
        "Krugs":{
            "Big":{
                gold_table: [15],
                xp_table: [15, 15.38, 16.13, 18, 19.5, 21.75]
            },
            "Medium":{
                gold_table: [10],
                xp_table: [10, 10.25, 10.75, 12, 13, 14.5]
            },
            "Small":{
                gold_table: [14],
                xp_table: [10, 10.25, 10.75, 12, 13, 14.5]
            }
        },
        "Scuttle":{
            gold_table: [100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 210, 220],
            xp_table: [55, 57.75, 60.5, 63.25, 66, 68.75, 71.5, 74.25, 77, 82.5, 88, 93.5, 99, 104.5, 110, 115.5, 121]
        }
    }

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

    