
#each indice in each table represents how much resource is given at that camp's level
camps = {
        "Gromp":{
            gold_table: [],
            xp_table: []
        },
        "Blue":{
            gold_table: [],
            xp_table: []
        },
        "Wolves":{
            gold_table: [],
            xp_table: []
        },
        "Raptors":{
            gold_table: [],
            xp_table: []
        },
        "Red Buff":{
            gold_table: [],
            xp_table: []
        },
        "Krugs":{
            gold_table: [],
            xp_table: []
        },
        "Scuttle":{
            gold_table: [],
            xp_table: []
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
    