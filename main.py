
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
#each level requries 100 more xp i.e. lvl 2 is 280 xp, 1v1 3 takes 380 xp, but 660 cumulative
class Champion():
    champion_xp = 0
    champion_gold = 0

    def get_champion_gold(self):
        return self.champion_gold

    def get_champion_xp(self):
        return self.champion_xp

    def get_champion_level(self):
        return (self.champion_xp-80)//100

    def increment_exp(self, increment):
        champion_xp += incremenet
    
    def increment_champion_gold(self, increment):
        champion_gold += increment
    
    def kill_camp(self, camp):
        self.increment_champion_gold(camp.get_camp_gold())
        self.increment_exp(camp.get_camp_xp())
    